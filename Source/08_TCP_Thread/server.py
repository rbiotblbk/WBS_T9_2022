import socket
import threading

print("Server Side with Thread")
print("*" * 30)


# Show Machine Name
server = socket.gethostname()
print(server) # DESKTOP-BN340OI  --> Name of the PC

# Show Machine IP
server = socket.gethostbyname(socket.gethostname())  
print(server)  # 192.168.178.53


PORT = 30000
BASIC_MSG_LEN = 64 # 64x bytes
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


ip = "" # receive from all IPs

ADDR = (ip,PORT)

# Create the Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Server Binding
server.bind(ADDR)

def handle_client(conn,addr):
    print("New Connection from the address:", addr)

    connected = True 

    while connected:

        # waits for the message length which will the client send
        msg_len = conn.recv(BASIC_MSG_LEN).decode(FORMAT)

        if msg_len: # if available
            msg_len = int(msg_len)

            # Wait for a message with the msg_len
            msg = conn.recv(msg_len).decode(FORMAT)

            # Show the received message
            print(f"[{addr}]   {msg}")

            # Send a confirmation message
            conn.send("Message received".encode(FORMAT))

            if msg == DISCONNECT_MSG:
                connected = False
    conn.close()



def app():
    server.listen()

    while True:
        # Wait for data from clients

        conn,addr = server.accept()

        # If a connections comes, create a new thread
        thread = threading.Thread(target=handle_client, args=(conn,addr))

        thread.start()

        print("Active Connections:", 
        threading.active_count() -1)


if __name__ == "__main__":
    app()
