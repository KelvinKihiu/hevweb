from hevweb.pipeline.static import StaticMiddleware
from hevweb.pipeline.routes import RouterMiddleware
from hevweb.pipeline.gzip import GzipMiddleware
from manage.routes import urls


#Configure application pipeline
#Add middleware here i.e. app = Middleware(app)
def configure_pipeline(app):

	#use routing middleware
	app = RouterMiddleware(app, urls)

	#use static middleware
	app = StaticMiddleware(app, cache_max_age=315576000)

	#use gzip middleware
	app = GzipMiddleware(app, compress_level=6)

	#Add more middleware here

	return app