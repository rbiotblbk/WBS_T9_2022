""" 
SMTP : Simple Mail Transfer Protocol
Only for ASCII Encoding
"""

import os
from pathlib import Path 
import smtplib
import json


os.chdir(Path(__file__).parent)

# Read Credentials from JSON File
with open("./email.json", mode = "r", encoding= "UTF-8") as f:
    json_text = f.read()

json_dict = json.loads(json_text)



# Define Credentials
gmail_user = json_dict["gmail_user"]
gmail_password = json_dict["gmail_pass"]

# Meta Data 

send_from = gmail_user
send_to = [gmail_user] # List of receivers

subject =  "Test E-Mail 1"
body = "Hello Body"



email_text = """\
From: {}   
To: {}
Subject: {}
{}
""".format(send_from, ", ".join(send_to), subject, body)

print(email_text)



try:
    # 1. Create Server 
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465) # port: 465

    # 2. Start Connection
    server.ehlo()

    # 3. Login 
    server.login(gmail_user, gmail_password)

    # 4. Send the E-Mail
    server.sendmail(send_from, send_to, email_text)

    # 5. Close the connection
    server.close()


    print("Sent Successfully!")



except Exception as e:
    print("Something went wrong!. \n ", e) 