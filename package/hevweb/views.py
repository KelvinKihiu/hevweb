import sys
import jinja2
from hevweb.config import get_configuration
import inspect
import os

def view(dict, view_name=None):
	if view_name == None:
		frame = inspect.stack()[1]
		module = inspect.getmodule(frame[0])
		filename = os.path.splitext(os.path.basename(module.__file__))[0]
		funcName = frame[3]
		view_name = f"{filename}/{funcName}.html"
	
	views_dir = get_configuration("VIEWS_DIR")

	view_loader = jinja2.FileSystemLoader(searchpath = views_dir)

	view_env = jinja2.Environment(loader = view_loader)

	view = view_env.get_template(view_name)

	output = view.render(dict)

	return output