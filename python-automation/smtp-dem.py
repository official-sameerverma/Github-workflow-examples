import smtplib
from email.mime.text import MIMEText

def send_email(subject,body):
    sender_email=""
    receiver_mail=""
    password=""

    msg=MIMEText(body)
    msg['subject']=subject
    msg['from']=sender_email
    msg['to']=receiver_mail

    with smtplib.SMTP("smtp.gmail.com", "587") as server:
        server.starttls()
        server.login(sender_email,password)
        server.send_message(msg)
        print("Message Send Sucessfully")
        print(msg)
        print(type(msg))


send_email("TEST", "HELLO MY NAME IS SAMEER. ")

