from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from views import app
from models import db


app.config.from_object('config.Development')
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
