from hevweb.controllers import view_controller
from hevweb.views import view


@view_controller
def index(req):
	return view({'title': 'Home'})


@view_controller
def about(req):
	return view({'title': 'About'})

@view_controller
def contact(req):
	return view({'title': 'Contact'})