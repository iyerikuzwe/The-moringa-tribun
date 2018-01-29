from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_mail(name ,reciever):
    #creating the subject of the message and the sender
    subject = "Welcome to the Amazing Moringa Tribune"
    sender = 'moringatribune33@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/newsemail.txt',{"name":name})
    html_content = render_to_string('email/newsemail.html',{"name":name})

    msg = EmailMultiAlternatives
    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()