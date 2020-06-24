import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    THREADED = True
    SECRET_KEY = b'I\x97\xcf}\x1eN$a[$\xf2\xfdT\xf1C\xf5\xb4\xeb\x97)\x19\x0eY\xab'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://iec_desenv:iec_desenv@localhost:5432/flask_contacts'


class Development(Config):
    DEBUG = True


class Testing(Config):
    # SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///' + os.path.join(basedir, 'testing.db')
    pass


config = {
    'dev': Development,
    'testing': Testing,
}
