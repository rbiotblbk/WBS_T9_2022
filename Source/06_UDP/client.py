import socket

print("Client Side UDP")
print("~" * 30)


# Create Socket
# AF_INET: IPV4
# SOCK_DGRAM : UDP


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "localhost" # IP of the server Localhost IP 127.0.0.1
port = 10000

# Create the message
message = input("Enter your message: ")

# Send the message
s.sendto(message.encode(), (ip,port))

# Close the socket
s.close()