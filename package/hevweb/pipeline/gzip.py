from hevweb.core import AppServer
from paste.gzipper import make_gzip_middleware


class GzipMiddleware(AppServer):
    """
    Middleware for gzipping the responses
    """
    def __init__(self, app, compress_level=6):
        self.app = app
        self.compress_level = compress_level

    def __call__(self, environ, start_response):
        return make_gzip_middleware(self.app, environ, compress_level=self.compress_level)(environ, start_response)