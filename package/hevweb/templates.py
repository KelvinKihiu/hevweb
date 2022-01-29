import os
import tempita


def render(template, **vars):
	if isinstance(template, str):
		caller_location = sys._getframe(1).f_globals['__file__']
		filename = os.path.join(os.path.dirname(caller_location), template)
		template = tempita.HTMLTemplate.from_filename(filename)
	vars.setdefault('request', get_request())
	return template.substitute(vars)