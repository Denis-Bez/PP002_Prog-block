# Flask libraries
from flask import Flask, render_template, redirect, flash, url_for, session, request, abort
from flask_sqlalchemy import SQLAlchemy

# Configuratins and castom libraries
from config import CONFIG
from site_elements import menu, content
from Class_SQLAlchemy import db, Menu, SEO, projects, Index, contacts, services

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
    return render_template('index.html', general=get_general_content(''), content=get_content('Index'))


# --- Dynamic pages ---
@application.route('/<main>/')
def Main(main):
    # if article == None:
    #   abort(404)
    return render_template(main + '.html', general=get_general_content(main), content=get_content(main))


@application.route('/projects/<project_name>/')
def project(project_name):
    content = projects.query.filter_by(visibility='visible', language='ru', url_name=project_name).first()
    return render_template('layout_project.html', general=get_general_content(project_name), content=content)

# @application.route('/services/<service_name>')
# def services(service_name):
#     return 'Страницы услуг'
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

def get_general_content(url_name):
    res = {}
    try:
        res['Menu'] = Menu.query.filter_by(visibility='visible', language='ru').order_by(Menu.priorities).all()
        res['SEO'] = SEO.query.filter_by(language='ru', url_name=url_name).first()
        return res 
    except:
        # TODO separate Heandler and sending report to mail
        return redirect ('/')


def get_content(page):
    try:
        res = eval(page).query.filter_by(visibility='visible', language='ru').all()
        return res 
    except Exception as a:
        # TODO separate Heandler and sending report to mail
        # Not right. Returned responose object
        return redirect ('/')


if __name__ == "__main__":
    application.run(debug=True)