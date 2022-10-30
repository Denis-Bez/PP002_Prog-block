import re

from flask import flash
from flask_mail import Message

from extensions import mail
from spam_list import spam_filter
from text_for_mail import mail_text


# Class for sending notification to clients and me about order, spam filter
class Mail:

    def __init__(self, form, lang):
        # Data from form
        self.contacts = form.get("contacts")
        self.text = form.get("text")
        # Text templates for message (Russia and English)
        self.mail_text = mail_text[lang]
        


    # It send order's information to me
    def send_message(self):
        try:
            msg_tome = Message("Order for development", recipients=["zakaz@worldcadabra.com"])
            msg_tome.body = "Client's contacts: {}\nOrder's text: {}\n".format(self.contacts, self.text)
            mail.send(msg_tome)
            flash(self.mail_text['success_flash'], category="success")
        except Exception as e:
            flash(self.mail_text["error_flash"], category="danger")
            msg_error = Message("Error on site worldcadabra.com", recipients=['v417459@yandex.ru'])
            msg_error.body = f"Error sending order's data to mail zakaz@worldcadabra.com. Error code: {e}"
            mail.send(msg_error)


    def spam_filter(self):
        try:
            # Check for empty
            if self.contacts and self.text:
                # Spam checking
                for spam_text in spam_filter["text"]:
                    if re.search(spam_text, self.text) or re.search(spam_text, self.contacts):
                        flash(self.mail_text["spam_flash"], category="danger")
                        return False
            else:
                flash(self.mail_text["spam_flash"], category="danger")
                return False
        except Exception as e:
            msg_error = Message("Error on site worldcadabra.com", recipients=["v417459@yandex.ru"])
            msg_error.body = (f"Spam filter error. Error code: {e}")
            mail.send(msg_error)
            return False
        return True

