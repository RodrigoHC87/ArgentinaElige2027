import os

from flask import Flask
from app.model import db
from config import Config

def crear_app():

    template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    app = Flask(__name__, template_folder=template_dir)
    app.config.from_object(Config)

    db.init_app(app)

    #- Establecer el contexto de la aplicación -#
    with app.app_context():
        db.create_all()

    # Registrar blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    return app
