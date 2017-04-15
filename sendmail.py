#!/usr/bin/#!/usr/bin/env python

import smtplib
import os

user = 'imoran@mail.ccsf.edu'
password = os.environ['MY_CCSF_PASS']

to = ['isismoran93@gmail.com']
subject = 'Hey, you'
body = 'Yes you (;'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (user, ", ".join(to), subject, body)

try:
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.login(user, password)
	server.sendmail(user, to, email_text)
	server.quit()
	print 'Email sent!'
except:
	print 'Something went wrong...'
