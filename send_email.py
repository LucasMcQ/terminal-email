#!/usr/bin/python

# Funtion: send_email_from_gmail()
# Returns: void
# Author: Lucas McQuiston
# Description: This function will send an email with the operation that was
# stored into the operation.txt file by the output of the read_email.py program.
# If operation that was in that file started with a '/' character, we know that
# the user emailed a path to a file that they would like sent to them, which
# the program will do. If the file did not start with a '/' character, then
# the user wanted the output of a particular terminal command, the program will
# then send the output of that particular command.


import smtplib
import time
import imaplib
import email

TO          = "INSERT EMAIL THAT YOU SEND COMMANDS FROM HERE"		# CHANGE THIS
FROM_EMAIL  = "INSERT EMAIL THAT WILL SEND YOU OUTPUT HERE"		# CHANGE THIS
FROM_PWD    = "PASSWORD OF EMAIL THAT WILL SEND YOU OUTPUT"		# CHANGE THIS 
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT   = 587


def send_email_from_gmail():

	# Save the operation to be performed into the operation var	
	with open('operation.txt', 'r') as myfile:
		operation = myfile.read()

	operation = operation[:-1]	# remove the newline at the end

	# If the operation starts with a '/' character, then we know the user
	# just wants a file to be sent.
	if operation.startswith('/'):
		with open(operation, 'r') as myfile:
			TEXT = myfile.read()
	# If the operation did not start with a '/' character, then the operation
	# is a bash command.
	else:
		TEXT = operation

	# The message that will be sent in the email.		
	message = TEXT

	# Send the email -- David Okwii
	# User: stackoverflow.com/users/547050/david-okwii
	# Post: stackoverflow.com/questions/1014755/how-to-send-email-with-gmail-as-provider-using-python
	try:
		
		server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
		server.ehlo()
		server.starttls()
		server.login(FROM_EMAIL, FROM_PWD)
		server.sendmail(FROM_EMAIL, TO, message)
		server.close()

	except Exception, e:
		print str(e)


send_email_from_gmail()
