""" 
IMAP : Internet Messasge Access Protocol Version 4
- Cerntral Orient EMails
- MailBoxes
- Multiple Devices
"""

import imaplib
import json 
import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


im = imaplib.IMAP4_SSL("imap.gmail.com", port = 993)


# Read Credentials from JSON File
with open("./email.json", mode = "r", encoding= "UTF-8") as f:
    json_text = f.read()

json_dict = json.loads(json_text)



# Define Credentials
gmail_user = json_dict["gmail_user"]
gmail_password = json_dict["gmail_pass"]


# Login Cred.
im.login(gmail_user, gmail_password)


# List of MailBoxes
print("Available Mail Boxes: ")


for mb in im.list()[1]:
    name = mb.split(b'"."')[-1]
    print(" - {}".format(name.decode().split(' "')))

# Ask the user which mail box
user_mb = input("Which Mailbox? ")

# Select the Mailbox
im.select(user_mb)


# Read the E-Mails in the choosed Mailbox
status, daten = im.search(None, "ALL")
print("Status:", status)
print("Daten:", daten)


# Loop Over the Emails
# RFC822: means the total message (Body and Header)

for mailnr in daten[0].split():
    typ, daten = im.fetch(mailnr, "(RFC822)")
    print("{}\n+++\n".format(daten[0][1].decode()))

im.logout()
im.close()
