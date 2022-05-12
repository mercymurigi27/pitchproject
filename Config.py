import os

class Config:
    SECRET_KEY = 'kittenarecute'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234 @localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'pitchesip@gmail.com'
    MAIL_PASSWORD = 'pitches123'

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1234 @localhost\p/pitch'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}    