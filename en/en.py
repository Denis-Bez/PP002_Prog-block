from flask import Blueprint, render_template, redirect

from site_elements import menu, content
from Class_SQLAlchemy import db, Menu

en = Blueprint('en', __name__, template_folder='templates', static_folder='static')

@en.route('/')
def index():
    return render_template('index.html', title='Main page', menu=menu['en'], content=content['en'], cont=get_content([Menu])) # 'en/index_en.html'


@en.route('/services')
def services():
    return 'Services'
@en.route('/parsers')
def parsers():
    return 'Parsers'
@en.route('/telegram_bots')
def telegram_bots():
    return 'Telegram bots'
@en.route('/webapp')
def webapp():
    return 'Web-Application'


@en.route('/projects')
def projects():
    return 'Projects'


@en.route('/contacts')
def contacts():
    return 'Contacts'


# --- DATBASE CONTENT GETTING ---

def get_content(tables):
    res = []
    try:
        for table in tables:
            res.append(table.query.filter_by(visibility='visible', language='ru').order_by(table.priorities).all())
        return res 
    except:
        # TODO separate Heandler and sending report to mail
        redirect ('/')
    
    