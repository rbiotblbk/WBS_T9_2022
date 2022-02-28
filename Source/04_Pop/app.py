""" 
POP3: Post Office Protocol  Version3 

"""

import poplib 
import json 
import os
from pathlib import Path 

os.chdir(Path(__file__).parent)


# Read Credentials from JSON File
with open("./email.json", mode = "r", encoding= "UTF-8") as f:
    json_text = f.read()

json_dict = json.loads(json_text)



# Define Credentials
gmail_user = json_dict["gmail_user"]
gmail_password = json_dict["gmail_pass"]



pop = poplib.POP3_SSL("pop.gmail.com", port = 995)

pop.user(gmail_user)
pop.pass_(gmail_password)


print(pop.stat())  # Tuple (Anzahl von Emails, Größe des Posteingangs)

# Loop over the Mails

for i in range(1, pop.stat()[0]+ 1):
    print(pop.retr(i)) # Tuple ( asnwer, line, length)

    print("+" * 30)

    for line in pop.retr(i)[1]: # line
        print(line)
    

    print("#" * 70)

pop.quit()