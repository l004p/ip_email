import smtplib, ssl
from subprocess import PIPE, Popen
from email.mime.text import MIMEText

with Popen("dig +short myip.opendns.com @resolver1.opendns.com", stdout=PIPE, stderr=None, shell=True) as process:
    output = process.communicate()[0].decode("utf-8")

receiver = "sampleemail@email.com"
sender = "testemail@outlook.com"
password = input('Login Password:')

message = MIMEText(output)
message['Subject'] = 'SUBJECT'
message['From'] = sender
message['To'] = receiver

context = ssl.create_default_context()

with smtplib.SMTP("smtp-mail.outlook.com", "587") as server:
    server.starttls(context=context)
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())
