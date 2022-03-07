
import requests

URL = "https://httpbin.org/basic-auth/usermohamed/passtesting"

username = "usermohamed"
password = "passtesting"


# Basic Authentication with the API
r = requests.get(URL, auth=(username,password))

print(r)