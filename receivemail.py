#!/usr/bin/#!/usr/bin/env python

import imaplib
import os
from email.parser import HeaderParser

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

    print raw_email

# including headers and alternate payloads
except:
	print "Sorry there was a problem connecting to your account"


# mail = imaplib.IMAP4_SSL('imap.gmail.com')
# mail.login('myemail@gmail.com', 'password123')
# mail.list()
# # Out: list of "folders" aka labels in gmail.
# mail.select("inbox") # connect to inbox.
#
# result, data = mail.search(None, "ALL")
#
# ids = data[0] # data is a list.
# id_list = ids.split() # ids is a space separated string
# latest_email_id = id_list[-1] # get the latest
#
# result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
#
# raw_email = data[0][1] # here's the body, which is raw text of the whole email
# # including headers and alternate payloads
#
#








# result, data = mail.search(None, "ALL")
#
# ids = data[0] # data is a list.
# id_list = ids.split() # ids is a space separated string
# latest_email_id = id_list[-1] # get the latest
#
# result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
#
# raw_email = data[0][1] # here's the body, which is raw text of the whole email
# # including headers and alternate payloads


# search_criteria = 'REVERSE DATE'
