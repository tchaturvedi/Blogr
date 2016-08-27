from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from main.views import page_not_found  # to render a custom 404 template

from main.views import main_template
from users.views import users_template

app = Flask(__name__)
db  = SQLAlchemy(app)
bcrypt = Bcrypt(app)


app.config.from_object('config.Development')

app.register_blueprint(main_template)
app.register_blueprint(users_template)
app.register_error_handler(404, page_not_found)

print(app.url_map)


from logging import FileHandler, WARNING
file_handler = FileHandler('log.txt')
file_handler.setLevel(WARNING)
app.logger.addHandler(file_handler)

db.create_all()
app.run('0.0.0.0')
