#!/Users/joelvogt/PyCharmProjects/citizenscience.coop/flask/bin/python

import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from webapp import app

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger=False,
    use_reloader=True,
    host='0.0.0.0',
    port=8080)
)

if __name__ == "__main__":
    manager.run()