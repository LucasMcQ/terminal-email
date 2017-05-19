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

VERIFIED_EMAIL = "RECIVING EMAIL ADDRESS"
FROM_EMAIL     = "SENDING EMAIL ADDRESS"
FROM_PWD       = "SENDING EMAIL PASSWORD"
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

					# msg['from'] stores the email address
					# in the format: name <email@domian.com>
					# this following code will extract the
					# email address and store it in the var
					# full_email and then compare it to the
					# verified email address.

					full_email = ""		# this will store the parsed email

					i = email_from.find('<') + 1 

					while email_from[i] != '>' :
						full_email += email_from[i]
						i = i + 1


					# This is to prevent other email addresses
					# from getting information on your computer...
					if full_email == VERIFIED_EMAIL:
						print 'Operation : ' + email_subject

	except Exception, e:
		print str(e)


read_email_from_gmail()
