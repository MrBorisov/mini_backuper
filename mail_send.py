import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config


def send_err(mesg):
    # create message object instance
    msg = MIMEMultipart()

    message = mesg

    # setup the parameters of the message
    subject = config.get_setting('area', 'area_name')
    password = config.get_setting('mail', 'smtp_pwd')
    msg['From'] = config.get_setting('mail', 'mail_from')
    msg['To'] = config.get_setting('mail', 'mail_to')
    msg['Subject'] = subject

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # create server
    srv = config.get_setting('mail', 'mysmtp')
    port = config.get_setting('mail', 'smtp_port')
    server = smtplib.SMTP(f'{srv}: {port}')

    server.starttls()

    # Login Credentials for sending the mail
    server.login(msg['From'], password)

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print
    "successfully sent email to %s:" % (msg['To'])
