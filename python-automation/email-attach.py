import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders


def send_email(subject,body, attched):
    sender_email="sameerverma8638@gmail.com"
    receiver_mail="awsamverma@gmail.com"
    password="xkqmvcajsuwcgbjl"

    msg=MIMEMultipart()
    msg['subject']=subject
    msg['from']=sender_email
    msg['to']=receiver_mail

    msg.attach(MIMEText(body))
    filename=attched


    with open(filename, 'rb') as attachment:
        mime_base=MIMEBase("application","octet-stream")
        mime_base.set_payload(attachment.read())


    encoders.encode_base64(mime_base)
    mime_base.add_header('content-disposition', 'attachment', filename='bank_statment.log')
    msg.attach(mime_base)

    with smtplib.SMTP("smtp.gmail.com", "587") as server :
        server.starttls()
        server.login(sender_email,password)
        server.send_message(msg)
        print("message sent successfully") 


send_email("TEST", "HELLO MY NAME IS SAMEER. ","D:\VS Code\myfolder\python-automation\app.log")