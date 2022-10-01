from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_mail import Mail, Message

from config import CONFIG


db = SQLAlchemy()

application = Flask(__name__)
application.config["SECRET_KEY"] = CONFIG['FLASK_SECRET_KEY']
application.config["MAIL_DEFAULT_SENDER"] = CONFIG["MAIL_DEFAULT_SENDER"]
application.config["MAIL_PASSWORD"] = CONFIG["MAIL_PASSWORD"]
application.config["MAIL_PORT"] = 465
application.config["MAIL_SERVER"] = "mail.worldcadabra.com"
application.config["MAIL_USE_TLS"] = False
application.config["MAIL_USE_SSL"] = True
application.config["MAIL_USERNAME"] = CONFIG["MAIL_USERNAME"]
mail = Mail(application)



# For creating tables need input that commands in Python's consol
# from extensions import create_app
# from Class_SQLAlchemy import *
# db.create_all(app=create_app())
def create_app():
    application = Flask(__name__)
    application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(application)

    return application