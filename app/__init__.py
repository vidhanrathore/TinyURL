from flask import Flask
from flask_mysqldb import MySQL

import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

mysql = MySQL()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY')
    app.config.from_object('config.DB_CONFIG')

    mysql.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app