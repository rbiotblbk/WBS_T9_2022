import socket
 

print("Client Side with Thread")
print("*" * 30)

PORT = 30000
BASIC_MSG_LEN = 64 # 64x bytes
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


ip = "localhost" # receive from all IPs

ADDR = (ip,PORT)

# Create the Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Client Connent 
client.connect(ADDR)


def send(message):

    message = message.encode(FORMAT)

    # Calculate the length of the message
    msg_len = len(message)
    msg_len = str(msg_len).encode(FORMAT)

    # Padding the msg length to reach the BASIC_MSG_LEN
    msg_len += b" " * (BASIC_MSG_LEN - len(msg_len))


    # 1. Send the length of the message
    client.send(msg_len)

    # 2. Send the message itself
    client.send(message)

    # Receive and print the confirmation message from the server
    print(client.recv(1024).decode(FORMAT))


send("Hallo Sara")
send(DISCONNECT_MSG)