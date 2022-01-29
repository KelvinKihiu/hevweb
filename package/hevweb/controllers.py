from keyword import kwlist
from webob import Request, Response
from webob import exc

#decorator for view controllers
def view_controller(func):
	def wrap_veiw(environ, start_response):
		req = Request(environ)
		try:
			resp = func(req, **req.urlvars)
		except exc.HTTPException as e:
			resp = e

		if isinstance(resp, str):
			resp = Response(body = resp)
		return resp(environ, start_response)
	return wrap_veiw


#decorator for api controllers
def api_controller(func):
	def wrap_veiw(environ, start_response):
		req = Request(environ)
		try:
			resp = func(req, **req.urlvars)
		except exc.HTTPException as e:
			resp = e

		resp = Response(json_body=resp)

		return resp(environ, start_response)
	return wrap_veiw