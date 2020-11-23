from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from main import *
from main.api import blueprint
from main.model.model import *

app = create_app('development')

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

"""
	Customized commands to be used to launch the application and database
	run: launch the backend api
	drop_all: drop all the existing tables at database
	create_all: create all the tables at database
"""


@manager.command
def run():
    app.run()


@manager.command
def drop_all():
    db.drop_all()


@manager.command
def create_all():
    db.create_all()


if __name__ == '__main__':
    manager.run()