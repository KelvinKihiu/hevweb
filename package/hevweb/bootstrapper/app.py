import os
import sys
from hevweb.execute_command import execute_command
from manage.config import create_app_server

if __name__ == '__main__':
	#Register the configurations
	os.environ.setdefault("APP_CONFIG", "manage.config")

	#create the application server
	app = create_app_server()

	#execute the command
	execute_command(sys.argv, app)