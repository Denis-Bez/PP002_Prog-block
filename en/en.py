import re

from flask import Blueprint, render_template, abort, redirect, request, flash
from flask_mail import Mail, Message

from Class_SQLAlchemy import db, Menu, SEO, projects, Index, contacts, services
from spam_list import spam_filter

from extensions import mail

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
        # Getting client's date from form
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        text = request.form.get("text")
        # Create text for sending message
        msg = Message("Order development", recipients=["v417459@yandex.ru"])
        msg_client = Message("Order was sent success", recipients=[email])
        msg_client.body = ("We was get your order") 
        # Spam filter
        try:
            for spam_text in spam_filter["text"]:
                if re.search(spam_text, text):
                    flash("Order identification as spam", category="danger")
                    return redirect ("/")
        except:
            msg_error = Message("Error on eg59.ru", recipients=["v417459@yandex.ru"])
            msg_error.body = ("Spam-filter Error")
            mail.send(msg_error)
            print("text: 'None'")
        # Sending mail
        try:
            mail.send(msg_client)
            status = "Confirmation was sent"
        except:
            status = "Confirmation don't sent"
        msg.body = (f"Client's Name: {name}\nClient's Telephone: {phone}\nEmail: {email}\nOedre's text: {text}\nStatus: {status}")      
        try:
            mail.send(msg)
            flash("Order was sent", category="success")
        except:
            flash("An error has occurred", category="danger")        
    return redirect ("/")


# --- DATBASE CONTENT GETTING ---
def get_general_content(url_name):
    res = {}
    try:
        res['Menu'] = Menu.query.filter_by(visibility='visible', language='en').order_by(Menu.priorities).all()
        res['SEO'] = SEO.query.filter_by(language='en', url_name=url_name).first()
        return res 
    except:
        abort(404)
    
    