#!/usr/bin/python

# Funtion: read_email_from_gmail()
# Returns: void
# Author: Lucas McQuiston
# Description: This function will read all of the emails sent to FROM_EMAIL
# and if the email address that sent an email to FROM_EMAIL is the same as the
# VERIFIED_EMAIL then it will print the operation out to stdout. Valid commands
# must be only sent in the subject portion of the email. Valid commands are either
# a path to a particular file that you would like sent to you, or a valid terminal
# command (this will send you the output of the command that you typed).
# Most of this function was copied from:
# codehandbook.org/how-to-read-email-from-gmail-using-python/

import smtplib
import time
import imaplib
import email

VERIFIED_EMAIL = "INSERT THE NAME ASSOCIATED WITH EMAIL ADDRESS <INSERT EMAIL ADDRESS THAT YOU WANT TO RECIVE TO>"	# ex: John Doe <johnDoe3425@gmail.com>
FROM_EMAIL     = "INSERT EMAIL THAT WILL SEND YOU OUTPUT HERE"		# CHANGE THIS
FROM_PWD       = "PASSWORD OF EMAIL THAT WILL SEND YOU OUTPUT"		# CHANGE THIS 
SMTP_SERVER    = "imap.gmail.com"
SMTP_PORT      = 993


def read_email_from_gmail():

	try:

		mail = imaplib.IMAP4_SSL(SMTP_SERVER)
		mail.login(FROM_EMAIL, FROM_PWD)
		mail.select('inbox')


		type, data = mail.search(None, 'ALL')
		mail_ids = data[0]


		id_list = mail_ids.split()
		first_email_id = int(id_list[0])
		latest_email_id = int(id_list[-1])


		for i in range(latest_email_id, first_email_id, -1):

			typ, data = mail.fetch(i, '(RFC822)' )

			for response_part in data:

				if isinstance(response_part, tuple):
					
					msg = email.message_from_string(response_part[1])
					email_subject = msg['subject']
					email_from = msg['from']

					# This is to prevent other email addresses
					# from getting information on your computer...
					if email_from == VERIFIED_EMAIL:
						print 'Operation : ' + email_subject

	except Exception, e:
		print str(e)


read_email_from_gmail()
