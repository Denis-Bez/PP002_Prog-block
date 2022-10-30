from flask import Blueprint, render_template, abort, request, redirect

from Class_SQLAlchemy import db, Menu, SEO, projects, Index, contacts, services

from Class_Mail import Mail

en = Blueprint('en', __name__, template_folder='templates', static_folder='static')

# HEANDLER BLOCK
# --- Static pages ---
@en.route('/')
def index():
    content = Index.query.filter_by(visibility='visible', language='en').first()
    return render_template('index.html', general=get_general_content(''), content=content)


@en.route('/projects/')
def Projects():
    content = projects.query.filter_by(visibility='visible', language='en').order_by(projects.priorities.desc()).all()
    return render_template('projects.html', general=get_general_content('projects'), content=content)


# --- Dynamic pages ---
@en.route('/<main>/')
def main(main):
    try:
        content = eval(main).query.filter_by(visibility='visible', language='en', url_name=main).first()
    except:
        abort(404)
    return render_template(main + '.html', general=get_general_content(main), content=content)


@en.route('/projects/<project_name>/')
def project(project_name):
    content = projects.query.filter_by(visibility='visible', language='en', url_name=project_name).first_or_404()
    return render_template('layout_project.html', general=get_general_content(project_name), content=content)


@en.route('/services/<service_name>/')
def service(service_name):
    content = services.query.filter_by(visibility='visible', language='en', url_name=service_name).first_or_404()
    return render_template('layout_service.html', general=get_general_content(service_name), content=content)


# Errors processing
@en.errorhandler(404)
def pageNotFound(error):
    return render_template('page_not_found.html', general=get_general_content('404')), 404


# --- Actions ---
@en.route("/email", methods=["POST", "GET"])
def email():
    if request.method == "POST":
        mail = Mail(request.form, 'en')
        if mail.spam_filter():
            mail.send_message()
    return redirect ('/en')


# --- DATBASE CONTENT GETTING ---
def get_general_content(url_name):
    res = {}
    try:
        res['Menu'] = Menu.query.filter_by(visibility='visible', language='en').order_by(Menu.priorities).all()
        res['SEO'] = SEO.query.filter_by(language='en', url_name=url_name).first()
        return res 
    except:
        abort(404)
    
    