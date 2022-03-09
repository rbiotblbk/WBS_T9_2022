# Local/Own Server Port Scanner
# Simple and Slow 
import socket 
import sys 

import os 
from pathlib import Path 
import json 

os.chdir(Path(__file__).parent )

with open("./portscanner.json", mode="r", encoding="UTF-8") as file:
    content = file.read()
    app_json = json.loads(content)


target_ip = app_json["target_ip"]
port_start = app_json["port_start"]
port_end = app_json["port_end"]

open_ports = [] 

try:
    for port in range(port_start, port_end+1):
        net_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
        result = net_socket.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")

        net_socket.close()
        

except:
    print("Error")
    print("Program will be closed")
    sys.exit(0)