'''
Create an Application server
'''

class AppServer(object):
	"""
		Creates an instance of Hevok App Server 
		that serves Application indefinitely.
	"""
	def __init__(self):
		self.status = '200 OK'


	def __call__(self, environ, start_response):
		#Build the response body
		response_body = '\n'.join(['%s: %s' % (key, value) for key, value in sorted(environ.items())])

		#Response headers
		response_headers = [ ('Content-Type', 'text/plain'), ('Content-Length', str(len(response_body))) ]

		#start the response
		start_response(self.status, response_headers)

		print(response_body)

		return [response_body]
