#!/usr/bin/#!/usr/bin/env python

import imaplib
import os

user = os.environ['MY_GMAIL_ACCT']
password = os.environ['MY_GMAIL_PASS']

try:
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(user, password)
	mail.list()
	mail.select('INBOX')
	result, data = mail.search(None, '(FROM "imoran@mail.ccsf.edu")')

	ids = data[0]
	id_list = ids.split()
	latest_email_id = id_list[-1]
	result, data = mail.fetch(latest_email_id, "(RFC822)")
	raw_email = data[0][1]

	message_content = raw_email[raw_email.find('Date'):]
	print message_content
except:
	print "There was a problem connecting to your account"
