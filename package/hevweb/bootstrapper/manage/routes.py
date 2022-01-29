'''
Create application's routes
'''
from hevweb.pipeline.routes import route



'''
you can also map the view_controller
from controllers.home import index
i.e. route('/url', view_controller=index)
'''
urls = [
	route('/', view_controller='home:index')
]