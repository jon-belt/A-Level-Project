from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from run import db
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

migrate = Migrate(app, db) #This instantiates the migrate module
manager = Manager(app) #This instantiates the manager module

manager.add_command('db',MigrateCommand) #This allows the module to be run via command prompt


if __name__ == '__main__': #If run, the manager will boot up
    manager.run()