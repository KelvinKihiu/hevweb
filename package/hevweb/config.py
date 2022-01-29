import importlib
import os


CONFIG_VAR = "APP_CONFIG"

def get_configuration(config_name):
	config = os.environ.get(CONFIG_VAR)

	config_mod = importlib.import_module(config)

	value = ''

	try:
		value = getattr(config_mod, config_name)
	except Exception as e:
		raise e

	return value