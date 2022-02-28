""" 
SMTP : Simple Mail Transfer Protocol
Only for ASCII Encoding
"""



""" 
MiMe Encoding provides:
- Special Chars, etc.
- Attachments
- HTML Template
"""

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


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

# E-Mail Container
message = MIMEMultipart()

# Email Meta Data
message["from"] = gmail_user
message["to"] = gmail_user
message["subject"] = "Mime Test 1"


# Body 
message.attach(MIMEText("This is a text E-Mail"))

# Attach an Image
message.attach(MIMEImage(Path("python.jpg").read_bytes()))



try: 
    with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as smtp:
        smtp.ehlo() # Start connection
        smtp.starttls()
        smtp.login(gmail_user, gmail_password)
        smtp.send_message(message)

        print("Sent Successfully !!")

except Exception as ex:
    print("Something went wrong !\n", ex)