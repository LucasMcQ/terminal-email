# Terminal Email

Author: Lucas McQuiston

# PURPOSE:
The purpose of this project is to send an email with some type of operation from
device A and and have device B send back the results of that specific operation.
There are two diffrent ways that you can perfrom operations.


# SETUP:
To set this up, you must hard code your email address and your email addresses
password in the fields provided in both the read_email.py and send_email.py
files.

# To run:
chmod +x search_email.sh
./search_email.sh


# HOW TO USE PROGRAM: 
All of the operations must be in the subject portion of the email being sent. It
is the only way it will work.

First option:
In the subject portion of the email, type the absolute path to a file that you
want emailed to you.

Example:
Subject: /home/user/mydirectory/myfile.txt

This will send the file 'myfile.txt' to your verified email.


Second option:
In the subject portion of the email, type a UNIX command.

Example:
Subject: ls -al /home/user/mydirectory

This will send the output of the UNIX command to your verified email.


# DIRECTIONS TO CONSTANTLY SEARCH FOR EMAIL:
If you want to have this script constantly running, you can use crontab to do so.

In a terminal type:
crontab -e

This will open up a text editor. Then place this line into the file:

*/1 * * * *  cd home/your-username/path-to-directory-with-files && ./search_email.sh

Save and exit.
This will run the script every minute.
