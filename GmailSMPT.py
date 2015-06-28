#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText
from random import randint

USERNAME = "@gmail.com"
PASSWORD = ""
MAILTO = ""

try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(USERNAME, PASSWORD)
        print("success")

except:
        print("failed")

for i in range(0,150): #spam
        msg = MIMEText("Hello Again")
        msg['Subject'] = ("Sent from Raspberry Pi "+str(randint(0,100000)))
        msg['From'] = USERNAME
        msg['To'] = MAILTO

        server.sendmail(USERNAME, MAILTO, msg.as_string())
        print("sent");
        if i==149:
                server.quit()
