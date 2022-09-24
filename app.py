# Flask libraries
from flask import Flask, render_template, flash, abort
from flask_mail import Mail, Message

# Configuratins and castom libraries
from config import CONFIG
from Class_SQLAlchemy import db, Menu, SEO, projects, Index, contacts, services

# Blueprint block
from en.en import en # English language site part


# CONFIGURATION BLOCK
SECRET_KEY = CONFIG['FLASK_SECRET_KEY']
application = Flask (__name__)
application.register_blueprint(en, url_prefix='/en')

application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(application)

application.config["MAIL_DEFAULT_SENDER"] = CONFIG["MAIL_DEFAULT_SENDER"]
application.config["MAIL_PASSWORD"] = CONFIG["MAIL_PASSWORD"]
application.config["MAIL_PORT"] = 465
application.config["MAIL_SERVER"] = "mail.eg-expert.ru"
application.config["MAIL_USE_TLS"] = False
application.config["MAIL_USE_SSL"] = True
application.config["MAIL_USERNAME"] = CONFIG["MAIL_USERNAME"]
mail = Mail(application)


# HEANDLER BLOCK
# --- Static pages ---
@application.route('/')
def index():
    content = Index.query.filter_by(visibility='visible', language='ru').all()
    return render_template('index.html', general=get_general_content(''), content=content)


@application.route('/projects/')
def Projects():
    content = projects.query.filter_by(visibility='visible', language='ru').all()
    return render_template('projects.html', general=get_general_content('projects'), content=content)


# --- Dynamic pages ---
@application.route('/<main>/')
def main(main):
    try:
        content = eval(main).query.filter_by(visibility='visible', language='ru', url_name=main).first()
    except:
        abort(404)
    return render_template(main + '.html', general=get_general_content(main), content=content)


@application.route('/projects/<project_name>/')
def project(project_name):
    content = projects.query.filter_by(visibility='visible', language='ru', url_name=project_name).first_or_404()
    return render_template('layout_project.html', general=get_general_content(project_name), content=content)


@application.route('/services/<service_name>/')
def service(service_name):
    content = services.query.filter_by(visibility='visible', language='ru', url_name=service_name).first_or_404()
    return render_template('layout_service.html', general=get_general_content(service_name), content=content)


# --- Errors processing ---
@application.errorhandler(404)
def pageNotFound(error):
    return render_template('page_not_found.html', general=get_general_content('404')), 404

# --- Actions ---
@application.route("/email", methods=["POST", "GET"])
def email():
    pass


# --- DATBASE CONTENT GETTING ---
def get_general_content(url_name):
    res = {}
    try:
        res['Menu'] = Menu.query.filter_by(visibility='visible', language='ru').order_by(Menu.priorities).all()
        res['SEO'] = SEO.query.filter_by(language='ru', url_name=url_name).first()
        return res 
    except:
        abort(404)

# --- START SERVER ---
if __name__ == "__main__":
    application.run(debug=True)