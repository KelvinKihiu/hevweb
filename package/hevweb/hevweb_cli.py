"""
hevweb
Usage:
    hevweb createapp [<args>]...
    hevweb -h | --help
    hevweb -v | --version
Options:
    -h, --help
    -v, --version
Example:
    hevweb createapp ApplicationName

"""

from inspect import getmembers, isclass

from docopt import docopt

from hevweb import __version__ as VERSION

def main():
    import hevweb.commands
    options = docopt(__doc__, version=VERSION)

    for (k, v) in options.items():
        if hasattr(hevweb.commands, k) and v:
            module = getattr(hevweb.commands, k)
            hevweb.commands = getmembers(module, isclass)
            command = [command[1] for command in hevweb.commands if command[0] != 'Base'][0]
            command = command(options)
            command.args = options['<args>']
            command.run()