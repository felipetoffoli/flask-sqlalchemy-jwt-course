class Config:
    SECRET_KEY = "BREIIIIIII"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:123@192.168.99.100/flask_contacts"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    Debug=True

class Testing(Config):
    pass

config = {
    "develoment": Development,
    "testing": Testing
}