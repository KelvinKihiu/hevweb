import sys
from hevweb.serve import serve

msg = """
app.py
Usage:
    app.py command [options]
    app.py -h | --help

Commands:
    serve   Starts the application server

Options:
    host    Server host (Optional)
    port    Port number to server the application (Optional)

Example:
    app.py serve <host> <port>

"""

def execute_command(args, app):
    if len(args) > 1:
        cmd = args[1]
        if cmd == 'serve':
            if len(args) == 4:
                serve(app, args[2], args[3])
            else:
                serve(app)
        elif cmd == '-h' or cmd == '--help':
            print(msg)
        else:
            print('"{}" command not found'.format(args[1]))
    else:
        print(msg)