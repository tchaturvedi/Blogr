class Development:
    DEBUG = True
    SECRET_KEY = '\x1a\xfc\x8b\x04\xeb\x08\x1c\x1f\xad\x84\xc7l\xf8tR\xd1\xc5v\xbd\x9dk\x92\xb8\x8b'
    SESSION_COOKIE_NAME = 'try_flask_session'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
