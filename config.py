import os

class Config:
    """Main configurations class"""


    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:kiplangat18@localhost/pitches'# os.environ.get("DATABASE_URL")

    SECRET_KEY = "try harder" #os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")





# class ProdConfig(Config):
#     """Production configuration class that inherits from the main configurations class"""
#     SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:kiplangat18@localhost/pitches'# os.environ.get("DATABASE_URL")
#     #SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace(
            "postgres://", "postgresql://", 1)

class DevConfig(Config):
    """Configuration class for development stage of the app"""
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
    #'test':TestConfig
}
