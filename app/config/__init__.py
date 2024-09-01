import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    FLASK_ENV = os.getenv('FLASK_ENV', 'production')
    DEBUG = FLASK_ENV == 'development'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True 

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False

config_by_name = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
)

def get_config():
    env_name = os.getenv('FLASK_ENV', 'production')
    return config_by_name.get(env_name, ProductionConfig)