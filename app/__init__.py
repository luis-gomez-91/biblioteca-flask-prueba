from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Instancias de las extensiones
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    from app import models

    # Inicialización de extensiones
    db.init_app(app)
    migrate.init_app(app, db)

    # Definición de rutas
    @app.route('/')
    def index():
        return render_template('index.html')

    return app