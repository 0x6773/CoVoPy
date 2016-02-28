#! /usr/bin/python2

import smtplib
from email.mime.text import MIMEText

def sendMail(user, pwd, to, subject, text):
    msg = MIMEText(text)
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject
    try:
        print 'HERE'
        smtpServer = smtplib.SMTP('smtp.gmail.com', 587)
        print '[ + ] Connecting to the Server.'
        smtpServer.ehlo()
        print '[ + ] Starting Encrypted Session.'
        smtpServer.startttls()
        smtpServer.ehlo()
        print '[ + ] Sending Mail.'
        smtpServer.sendmail(user, to, msg.as_string())
        smtpServer.close()
        print '[ + ] Mail Sent Successfully.'
    except:
        print '[ - ] Sending Mail Failed.'

user = 'username'
pwd = 'password'

sendMail(user, pwd, 'target@tgt.tgt', 'Re : Important', 'Test Message')
