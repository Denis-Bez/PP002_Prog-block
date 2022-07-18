from flask import Blueprint, render_template

from site_elements import menu, content

eng = Blueprint('eng', __name__, template_folder='templates', static_folder='static')

@eng.route('/')
def index():
    return render_template('index.html', title='Main page', menu=menu['eng'], content=content['eng']) # 'eng/index_eng.html'


@eng.route('/services')
def services():
    return 'Services'
@eng.route('/parsers')
def parsers():
    return 'Parsers'
@eng.route('/telegram_bots')
def telegram_bots():
    return 'Telegram bots'
@eng.route('/webapp')
def webapp():
    return 'Web-Application'


@eng.route('/projects')
def projects():
    return 'Projects'


@eng.route('/contacts')
def contacts():
    return 'Contacts'
    
    