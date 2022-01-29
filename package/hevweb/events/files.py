from watchdog.events import FileSystemEventHandler


class FileModifiedEventHandler(FileSystemEventHandler):
	"""docstring for FileModifiedHandler"""
	def on_modified(self, event):
		raise FileModifiedException("File modified")


class FileModifiedException(Exception):
	"""docstring for FileModifiedException"""