from views import app
from models import db

from logging import FileHandler, WARNING
file_handler = FileHandler('log.txt')
file_handler.setLevel(WARNING)
app.logger.addHandler(file_handler)

db.create_all()
app.run('0.0.0.0')
