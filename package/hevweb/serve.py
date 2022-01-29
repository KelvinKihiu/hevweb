import webbrowser
import datetime
from time import sleep
from paste import httpserver
from hevweb.config import get_configuration

def serve(app, host='127.0.0.1', port=8888):
	port = int(port)
	now = datetime.datetime.now()

	print('\Hevweb version 1.0.0')
	sleep(1)
	print(str(now))
	sleep(1)

	if webbrowser.open('http://{}:{}'.format(host, port)):
		print('Opening application in browser. Please wait...\n')


	print('Press Ctrl+C to exit the application\n')
	#sleep(1)

	try:
		httpserver.serve(app, host, port)
	except KeyboardInterrupt:
		print('\nShutting down the server...')
