import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = b"}\xe7\xbb':N\x0f:\x07\n\x7f*'\xbb;\xd4\x99\x06\xb0K\xb4\x01\xea\xeb"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False

class Development(Config):
    DEBUG = True


class Production(Config):
    pass


class Testing(Config):
    TESTING = True


config = {
    'development': Development,
    'production': Production,
    'testing': Testing,
}
