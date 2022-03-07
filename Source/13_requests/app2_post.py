import requests 

# POST (like a form)
#########################
payload = {"username": "mohamed", "password": "testing"}

URL = "https://httpbin.org/post"
r = requests.post(URL, data = payload)
print(r.text)

# Get the JSON Response
##########################

print(r.json())

# Get only the payload data from the request
print(r.json('form'))

