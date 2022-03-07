# pip install requests 

import requests
import os 

from pathlib import Path 

os.chdir(Path(__file__).parent)

# Download an image/file
####################

r = requests.get("https://imgs.xkcd.com/comics/python.png") # the will open the image in bytes

with open("myimage.png", mode = "wb") as f:
    f.write(r.content) # write bytes in wb mode

# Information
print("Status Code:", r.status_code) # 200
print("Status OK:", r.ok) # True 
print("Status Header", r.headers)
