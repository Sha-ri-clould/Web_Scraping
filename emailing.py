import smtplib
import ssl
import os

def mail(message):
    host = 'smtp.gmail.com'
    port = 465

    sender_email= os.getenv('EMAIL_ADDRESS')
    password = os.getenv('EMAIL_PASSWORD')

    receiver_email = os.getenv('RECEIVER_EMAIL')
    context = ssl.create_default_context()

    subject= "Tour Update Notification - Webscraping"
    body = "Hello! New Tour found."

    message = f"Subject: {subject}\n\n{body}\n{message}"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent")
        server.close()