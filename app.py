import re

# Flask libraries
from flask import Flask, render_template, flash, abort, redirect, request
from flask_mail import Mail, Message

# Configuratins and castom libraries
from config import CONFIG
from spam_list import spam_filter
from Class_SQLAlchemy import db, Menu, SEO, projects, Index, contacts, services
from extensions import mail, application

# Blueprint block   
from en.en import en # English language site part


# CONFIGURATION BLOCK
application.register_blueprint(en, url_prefix='/en')
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///content.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(application)


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
        # Getting client's date from form
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        text = request.form.get("text")
        # Create text for sending message
        msg = Message("Заявка на экспертизу", recipients=["v417459@yandex.ru"])
        msg_client = Message("Заявка успешно отправлена", recipients=[email])
        msg_client.body = ("Мы получили заявку на экспертизу. Свяжемся с вами в ближайшее время для уточнения информации") 
        # Spam filter
        try:
            for spam_text in spam_filter["text"]:
                if re.search(spam_text, text):
                    flash("Заявка распознана системой как спам! Попробуйте написать нам на почту office@eg59.ru или позвонить по телефону +7 (342) 200-85-05", category="danger")
                    return redirect ("/")
        except:
            msg_error = Message("Ошибка на сайте eg59.ru", recipients=["v417459@yandex.ru"])
            msg_error.body = ("Ошибка при работе спам-фильтра")
            mail.send(msg_error)
            print("text: 'None'")
        # Sending mail
        try:
            mail.send(msg_client)
            status = "Подтверждение на почту отправлено"
        except:
            status = "Подтверждение на почту не отправлено"
        msg.body = (f"Имя клиента: {name}\nТелефон клиента: {phone}\nEmail заявки: {email}\nТекст заявки: {text}\nСтатус отправки письма клиенту: {status}")      
        try:
            mail.send(msg)
            flash("Заявка успешно отправлена! Мы свяжемся с Вами в ближайшее время", category="success")
        except:
            flash("Произошла ошибка при отправке заявки. Попробуйте написать нам на почту expert@eg59.ru или позвонить по телефону +7 912-88-97-709", category="danger")        
    return redirect ("/")


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