

# Flask libraries
from flask import render_template, abort, redirect, request

# Configuratins and castom libraries
from config import CONFIG

from extensions import application
from Class_SQLAlchemy import Menu, SEO, projects, Index, contacts, services, db
from Class_Mail import Mail

# Blueprint block   
from en.en import en # English language site part
application.register_blueprint(en, url_prefix='/en')


# HEANDLER BLOCK
# --- Static pages ---
@application.route('/')
def index():
    content = Index.query.filter_by(visibility='visible', language='ru').first()
    return render_template('index.html', general=get_general_content(''), content=content)


@application.route('/projects/')
def Projects():
    content = projects.query.filter_by(visibility='visible', language='ru').order_by(projects.priorities.desc()).all()
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
    if request.method == "POST":
        mail = Mail(request.form, 'ru')
        if mail.spam_filter():
            mail.send_message()
    return redirect ("/")


# --- OTHER ---
@application.route('/yandex_bc89ba786bf33137.html')
def yandex_verification():
    return render_template('yandex_bc89ba786bf33137.html')

@application.route("/sitemap.xml")
def sitemap():
    return render_template('sitemap.xml')


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