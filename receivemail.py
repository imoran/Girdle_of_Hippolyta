#!/usr/bin/#!/usr/bin/env python

import imaplib
import os

user = 'isismoran93@gmail.com'
password = '100607isis'

try:
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(user, password)
    mail.list()
    mail.select('INBOX')
    result, data = mail.search(None, '(FROM "imoran@mail.ccsf.edu")')

    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string
    latest_email_id = id_list[-1] # get the latest
    result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
    raw_email = data[0][1] # here's the body, which is raw text of the whole email

    message_content = raw_email[raw_email.find('Date'):]
    print message_content
except:
	print "Sorry there was a problem connecting to your account"
