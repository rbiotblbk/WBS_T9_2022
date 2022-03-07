import urllib.request
import urllib.parse 

import os
from pathlib import Path 
os.chdir(Path(__file__).parent)

try:
    url = "https://www.google.com/search?q=python" 

    headers = {}

    # User agent identifies the website which browser (not as python)
    headers['User-Agent'] = 'Mozilla/5.0 (Linux; <Android Version>; <Build Tag etc.>) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>'
  
    # Add the headers to the request
    req = urllib.request.Request(url, headers=headers)

    # Get Response from the website
    response = urllib.request.urlopen(req)

    response_data = response.read()

    with open("result.txt", mode = "w", encoding= "UTF-8") as f:
        f.write(str(response_data))


except Exception as ex:
    print("Error: ", ex) 

