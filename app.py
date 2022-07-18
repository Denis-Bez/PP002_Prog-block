# Flask libraries
from flask import Flask, render_template, redirect, flash, url_for, session, request, abort
from flask_sqlalchemy import SQLAlchemy

# Configuratins and castom libraries
from config import CONFIG
from site_elements import menu, content

# Blueprint block
from eng.eng import eng # Enlish language site part

# Other libraries
from datetime import datetime


# CONFIGURATION BLOCK
SECRET_KEY = CONFIG['FLASK_SECRET_KEY']

application = Flask (__name__)
application.register_blueprint(eng, url_prefix='/eng')
application.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{CONFIG["Posgresql_password"]}@192.168.1.39:5432/base_name'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(application)

class Content_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text_block = db.Column(db.String(), unique=True)
    language = db.Column(db.String(10))
    position = db.Column(db.Integer)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<users {self.id}>'


# HEANDLER BLOCK
@application.route('/')
def index():
    
    # Вопрос как извлечь только строку с rus и index?
    cont = Content_table.query.all()

    return render_template('index.html', title='Главная страница', menu=menu['rus'], content=content['rus'])


@application.route('/services')
def services():
    return 'Услуги'

@application.route('/parsers')
def parsers():
    try:
        i = Content_table(text_block=content['eng']['index'], language='rus',
            position='0')
        db.session.add(i)
        db.session.commit()
        return 'Success!'
    except:
        db.session.rollback()
        print('Ошибка добавления в БД')
        return 'Bad'

@application.route('/telegram_bots')
def telegram_bots():
    return 'Telegram боты'
@application.route('/webapp')
def webapp():
    return 'Веб-приложения'


@application.route('/projects')
def projects():
    return 'Проекты'


@application.route('/contacts')
def contacts():
    return 'Контакты'


# Errors processing. Не перехватывает с подкатегорий типа '/test/<name>'?
@application.errorhandler(404)
def pageNotFound(error):
    return render_template('page_not_found.html', title='Страница не найдена', menu=menu['rus']), 404


if __name__ == "__main__":
    # db.create_all()
    application.run(debug=True)