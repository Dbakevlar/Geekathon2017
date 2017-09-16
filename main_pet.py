#!/usr/bin/python

#generic imports
import time
import gps
import gps_data
import gps_read
import os
import noble
import socket.io
import blescan
from time import sleep, strftime
from subprocess import *
from subprocess import call

#imports for email
import imaplib
import smtplib
import email
from email.mime.text import MIMEText
from email.parser import HeaderParser
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.Utils import COMMASPACE, formatdate
from email import Encoders


USERNAME = "dbakevlar@gmail.com"     #email addy   #!/usr/bin/env python
PASSWORD = "" 			#email password	

programpause = 5   #pause for x seconds
temp_list = []

##########################################
#FUNCTION FIND UNREAD EMAILS	
##########################################

def check_email():
    status, email_ids = imap_server.search(None, '(UNSEEN)')    #searches inbox 
    if email_ids == ['']:
        print('No Unread Emails')
        mail_list = []
    else:
        mail_list = get_senders(email_ids)
        print('List of email senders: ', mail_list)         #mark as read
        print len(mail_list),
        print("pet mail!")

    imap_server.close()
    return mail_list
	
##########################################
#FUNCTION PULL EMAIL ADDRESS	
##########################################

def get_senders(email_ids):
    senders_list = []          				   #create list 
    for e_id in email_ids[0].split():   		   #Loops new emails
    	resp, data = imap_server.fetch(e_id, '(RFC822)')   #fetch it
    	perf = HeaderParser().parsestr(data[0][1])	   #parse it
    	senders_list.append(perf['From'])		   #get from 
    return senders_list

##########################################
#FUNCTION SEND EMAILS
##########################################

def send_email(mail_list):
    for item in mail_list:
        files = []
        files.append("fillfile.py")
        text = 'Where is my owner?'
        assert type(files)==list
        msg = MIMEMultipart()
        msg['Subject'] = 'I miss you, Mommy!'
        msg['From'] = USERNAME
        msg['To'] = item

        msg.attach ( MIMEText(text) )  

        for file in files:
            part = MIMEBase('application', "octet-stream")
            part.set_payload( open(file,"rb").read() )
            Encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"'
                   % os.path.basename(file))
            msg.attach(part)


        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.ehlo_or_helo_if_needed()
        server.login(USERNAME,PASSWORD)
        server.sendmail(USERNAME, item, msg.as_string() )
        server.quit()
        print('Email sent to ' + item + '!')


##########################################
#FUNCTION TAKE VIDEO
##########################################

def takevideo():
    call(["uvccapture", "-v", "-S45", "-B190", "-C35", "-G50", "-x640", "-y480"])
    time.sleep(5)
    call(["uvccapture", "-v", "-S45", "-B190", "-C35", "-G50", "-x640", "-y480"])

##########################################
#FUNCTION GPS DATA
##########################################

def getgps():
    print 'service func'

if __name__ == '__main__':
    # capture gps data and verify vicinity via functions
    # decide to capture or sleep
    gps_read()
    gps_data()
    
##########################################
#FUNCTION RANGE SIGNAL
##########################################

def getrange():
    if gps_read(range(3) ==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    then makemsg()

##########################################
#FUNCTION CREATE MESSAGE 
##########################################

def makemsg():
    return_code = call(["ffplay", "-nodisp", "-autoexit", "../esme.wav"])
    # return_code = call(["aplay", "../gooddog.wav"])    
    print "Played successfully" if return_code == 0 else "Play ended in error"


##########################################
#PET IS IN RANGE, DO THE THING ZHU-LEE
##########################################

while True:
    homescreen()
    check = getrange() #raw_input("Type Yes to check email: ")
    if check  == "yes":
        print "Doing the thing ZHU-LEE"
        playmsg() 
        time.sleep(1)
        makemsg()
        imap_server = imaplib.IMAP4_SSL("imap.gmail.com",993)
        imap_server.login(USERNAME, PASSWORD)
        imap_server.select('INBOX')
        mail_list = check_email()
        temp_list = temp_list + mail_list
        if mail_list :
            send_email = raw_input("Send emails? (yes/no)")
            if sendemail == "yes":
		takevideo() 
                send_email(mail_list)
            else:
                print("OK,time to sleep ")
        else:
            print("OK, nothing to do")
            
    time.sleep(programpause)
    

