__author__ = 'python robot'

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

txtmsg = 'this is a mail sent by python robot... -_-!'
f = open('c:/Users/sancheng/PycharmProjects/session2/test/sendmail.py')
txtmsg = txtmsg + "\r\n source code : \r\n"  + f.read()

# Create a text/plain message
msg = MIMEText(txtmsg)

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'greetings from python robot, it is not a jun mail.'
msg['From'] = 'sancheng@cisco.com'
msg['To'] = 'newtech-hf-lang'

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('smtp.gmail.com')
s.sendmail('sancheng@gmail.com', ['sancheng@gmail.com'], msg.as_string())
s.quit()



