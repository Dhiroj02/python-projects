from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = "dhirojkumarsahu13@gmail.com"
email_password = password

email_reciver = "aalekika@gmail.com"

subject = "just a little reminder"
body = """
I love you 
"""
# instance of the email message

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())
