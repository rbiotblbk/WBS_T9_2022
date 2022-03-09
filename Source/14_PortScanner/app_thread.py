# Local/Own Server Port Scanner
# Thread but quick 

import threading 
import socket 
import sys
from queue import Queue  #  first  in first out
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

num_threads = 10
thread_list = []
open_ports = []

queue = Queue() 


def scan_port(port):
    net_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP
    result = net_socket.connect_ex((target_ip, port))
    if result == 0:
        return True
    else:
        return False

    


def worker():
    while not queue.empty():
        port = queue.get()
        if scan_port(port):
            # print(f"Port {port} is open")
            open_ports.append(port)
            
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)



if __name__ == "__main__":

    # Create a list of Ports
    port_list = range(port_start, port_end)

    # Fill the Queue with port list, to avoid scanning the same port via threads
    fill_queue(port_list)

    # Create and start the threads
    for t in range(num_threads):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print("Open Ports are:", open_ports)
    