import re
import sys
import threading
import urllib
from webob import Request
from webob import exc
from hevweb.config import get_configuration
from urllib.parse import parse_qsl, urlencode
from hevweb.core import AppServer
import datetime

var_regex = re.compile(r'''
	\{
	(\w+)
	(?::([^}]+))?
	\}
	''', re.VERBOSE)

def url_to_regex(url):
	regex = ''
	last_pos = 0
	for match in var_regex.finditer(url):
		regex += re.escape(url[last_pos:match.start()])
		var_name = match.group(1)
		expr = match.group(2) or '[^/]+'
		expr = '(?P<%s>%s)' % (var_name, expr)
		regex += expr
		last_pos = match.end()
	regex += re.escape(url[last_pos:])
	regex = '^%s$' % regex
	return regex



def load_view_controller(string):
	module_name, func_name = string.split(':', 1)
	controllers_dir = get_configuration('CONTROLLERS_DIR')
	path = list(sys.path)
	sys.path.insert(0, controllers_dir)
	func = None
	try:
		module = __import__(module_name)
		func = getattr(module, func_name)
	except Exception as e:
		raise e
	finally:
		sys.path[:] = path
	return func



class RouterMiddleware(AppServer):
	"""docstring for RouterMiddleware"""
	def __init__(self, app, urls=[]):
		self.app = app
		self.routes = []
		for url_tuple in urls:
			url, view_controller = url_tuple
			self.add_route(url, view_controller=view_controller)


	def add_route(self, url, view_controller, **vars):
		if isinstance(view_controller, str):
			view_controller = load_view_controller(view_controller)

		self.routes.append((re.compile(url_to_regex(url)), view_controller, vars))


	def __call__(self, environ, start_response):
		req = Request(environ)
		for regex, view_controller, vars in self.routes:
			match = regex.match(req.path_info)
			if match:
				req.urlvars = match.groupdict()
				req.urlvars.update(vars)
				return view_controller(environ, start_response)

		try:
			params = list(filter(None, req.path_info.split('/')))

			if len(params) > 1:
				view_controller = load_view_controller(params[0] + ':' + params[1])

				if environ['QUERY_STRING']:
					req.urlvars = dict(parse_qsl(environ['QUERY_STRING']))
					req.urlvars.update({})
					return view_controller(environ, start_response)
				else:
					if len(params) == 2:
						return view_controller(environ, start_response)
					elif len(params) == 3:
						req.urlvars = {'slug': params[2]}
						req.urlvars.update({})
						return view_controller(environ, start_response)
					else:
						return exc.HTTPNotFound()(environ, start_response)
			else:
				return exc.HTTPNotFound()(environ, start_response)
		except:
			return exc.HTTPNotFound()(environ, start_response)


class Localized(object):
	"""docstring for Localized"""
	def __init__(self):
		self.local = threading.local()

	def register(self, object):
		self.local.object = object

	def unregister(self):
		del self.local.object

	def __call__(self):
		try:
			return self.local.object
		except AttributeError:
			raise TypeError("No object has been registered for this thread")


get_request = Localized()


class RegisterRequest(object):
	"""docstring for RegisterRequest"""
	def __init__(self, app):
		self.app = app

	def __call__(self, environ, start_response):
		req = Request(environ)
		get_request.register(req)
		try:
			return self.app(environ, start_response)
		finally:
			get_request.unregister()

def url(*segments, **vars):
	base_url = get_request().application_url
	path = '/'.join(str(s) for s in segments)
	if not path.startswith('/'):
		path = '/' + path
	if vars:
		path += '?' + urlencode(vars)
	return base_url + path


def route(url, view_controller):
	return url, view_controller