import mimetypes
import os
import sys
from hevweb.config import get_configuration
from hevweb.core import AppServer
from webob import exc
from paste.urlparser import StaticURLParser


#static files server middleware
class StaticMiddleware(AppServer):
	"""
		Renders static files to the view
	"""
	def __init__(self, app, cache_max_age=0):
		self.app = app
		self.static_dir = get_configuration('STATIC_DIR')
		self.cache_max_age = cache_max_age


	def __call__(self, environ, start_response):
		path = ''
		if sys.platform == 'win32':	
			path = self.static_dir + environ['PATH_INFO'].replace('/','\\')
		else:
			path = self.static_dir + environ['PATH_INFO']
		
		if os.path.isfile(path):
			return StaticURLParser("static/", cache_max_age=self.cache_max_age)(environ, start_response)
		else:
			return self.app(environ, start_response)
		# path = self.static_dir + environ['PATH_INFO'].replace('/','\\')
		# filetype = mimetypes.guess_type(path, strict=True)[0]
		# if not filetype:
		# 	return self.app(environ, start_response)
		# else:
		# 	if not os.path.isfile(path):
		# 		return exc.HTTPNotFound()(environ, start_response)
		# 	else:
		# 		start_response("200 OK", [('Content-type', filetype), ('SERVER_SOFTWARE', 'Hevok/0.1'), ('HTTP_CACHE_CONTROL', 'public,max-age=1')])
		# 		return environ['wsgi.file_wrapper'](open(path, 'rb'), 4096)