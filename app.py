# Flask libraries
from flask import Flask, render_template, redirect, flash, url_for, session, request, abort
from flask_sqlalchemy import SQLAlchemy

# Configuratins and castom libraries
from config import CONFIG
from site_elements import menu, content
from Class_SQLAlchemy import db, Menu

# Blueprint block
from en.en import en # English language site part

# Other libraries
from datetime import datetime


# CONFIGURATION BLOCK
SECRET_KEY = CONFIG['FLASK_SECRET_KEY']
application = Flask (__name__)
application.register_blueprint(en, url_prefix='/en')

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(application)


# HEANDLER BLOCK
# --- Static pages ---
@application.route('/')
def index():
    return render_template('index.html', title='Главная страница', menu=menu['rus'], content=content['rus'], cont=get_content([Menu]))

@application.route('/projects')
def projects():
    return 'Проекты'

@application.route('/services')
def services():
    return redirect ('/')

@application.route('/contacts')
def contacts():
    return 'Контакты'


# --- Dynamic pages ---
@application.route('/<main>')
def object(main):
    content = get_content([Menu, ])
    # if article == None:
    #   abort(404)
    return 'Основные страницы сайта'
    # return render_template(main + '.html', content=get_content([main]))
    # return render_template(main + '.html', content=get_content([Menu]))

@application.route('/projects/<project_name>')
def object(project_name):
    return 'Страницы проектов'
    # return render_template('layout_project.html', content=get_content([Menu]))

@application.route('/services/<service_name>')
def object(project_name):
    return 'Страницы услуг'
    # return render_template('layout_service.html', content=get_content([Menu]))

# Errors processing. Не перехватывает с подкатегорий типа '/test/<name>'?
@application.errorhandler(404)
def pageNotFound(error):
    return render_template('page_not_found.html', title='Страница не найдена', menu=menu['rus']), 404
# Example from internet
# article = Article.query.get(article_id)
# if article == None:
#     abort(404)

# --- DATBASE CONTENT GETTING ---

def get_content(tables):
    res = []
    try:
        for table in tables:
            res.append(table.query.filter_by(visibility='visible', language='ru').order_by(table.priorities).all())
            # For pages
            # pages.query.filter_by(visibility='visible', language='ru').first()
            # For projects and services
            # table.query.filter_by(visibility='visible', language='ru', url_name=url_name).first()
            # For prewiev
            # table.query.filter_by(visibility='visible', language='ru').order_by(table.priorities).all()
        return res 
    except:
        # TODO separate Heandler and sending report to mail
        return redirect ('/')


if __name__ == "__main__":
    application.run(debug=True)