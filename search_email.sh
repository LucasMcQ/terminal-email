#!/bin/bash

# File: search_email.sh
# Author: Lucas McQuiston
# Description: This script will execute the read_email.py script and save all
# of the emails to a file named new_mail.txt. The most new operation that is in
# that file will be saved to a file named operation.txt. If there was a new email
# in the new_mail.txt file (this is known by comparing the contents of new_mail.txt
# and old_mail.txt using the diff command) then the send_email.py script will
# be executed to send the email to the user with the desired command output or
# the desired file that they wanted to recieve.


# Execute script to read emails. The output is directed into a file named
# new_mail.txt.
python read_email.py > new_mail.txt


# Create file if there was no file present (startup).
touch old_mail.txt

# Check to see if there is new mail.
diff new_mail.txt old_mail.txt > /dev/null 2>&1

# If there was no new mail then we will terminate the script.
if [[ $? -eq 0 ]]; then
	cp new_mail.txt old_mail.txt
	exit 0
fi


# Get the operation that we are interested in.
OPERATION="$(grep -m 1 ':' new_mail.txt | sed 's/^.*: //' | tr -d "\n")"

if [[ $OPERATION == /* ]]; then
	echo $OPERATION > operation.txt

# If user used a tilda to represent their home directory, then we will replace
# the tilda with their home directory.
elif [[ $OPERATION == ~* ]]; then
	TILDA_FIX="${OPERATION/"~"/$HOME}"
	echo $TILDA_FIX > operation.txt

# If the user wanted to enter a bash command.
else
	
	OPERATION_FIX=${OPERATION/"~"/$HOME}
	# Place the operation into a folder named operation.txt
	$OPERATION_FIX > operation.txt

	# If the command that was entered was not a valid command.
	if [[ $? -eq 127 ]]; then
		echo "INVALID COMMAND" > operation.txt
	fi

fi


# compare the new mail to old mail to see if there was a new message, and throw
# away any output that is produced.
diff new_mail.txt old_mail.txt > /dev/null 2>&1

# If there was a new email, then send the email.
if [[ $? -eq 1 ]]; then
	# Send the email with the output of the command, or the file that the
	# email sender wanted to recive.
	python send_email.py
fi

# Overwrite the old mail file with the new mail file. This is used to see if
# there is new mail the next time this script is executed.
cp new_mail.txt old_mail.txt

# Clean up files...
rm operation.txt
