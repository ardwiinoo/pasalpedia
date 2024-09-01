from flask import Flask
from app.routes.web import web_bp
from app.database import init_db
from app.config import get_config

def create_app():
    app = Flask(__name__, template_folder='./resources/views', static_folder='./resources/static')
    app.config.from_object(get_config())
    app.register_blueprint(web_bp)

    init_db(app)

    return app