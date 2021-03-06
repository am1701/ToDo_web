from django.core.mail import send_mail
from django.conf import settings

def send_email(assunto, message):
    subject = assunto
    message = message
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['djangosimples@gmail.com','Hermelio.ifma@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    return None
