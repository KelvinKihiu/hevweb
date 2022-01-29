import os
from hevweb.core import AppServer
from pipeline.configure import configure_pipeline


#Create an instance of the application
def create_app_server():
	#create the AppServer
	app = AppServer()
	#Configure the application's pipeline
	app = configure_pipeline(app)

	return app


#Application name
APP_NAME = 'APPLICATION_NAME'


#app directory
APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#views directory
VIEWS_DIR = os.path.join(APP_DIR, 'views')


#controllers directory
CONTROLLERS_DIR = os.path.join(APP_DIR, 'controllers')


#static directory
STATIC_DIR = os.path.join(APP_DIR, 'static')