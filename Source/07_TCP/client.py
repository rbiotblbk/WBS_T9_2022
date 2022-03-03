import socket

print("Client Side TCP")
print("~" * 30)


# Create Socket
# AF_INET: IPV4
# SOCK_STREAM : TCP


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = "localhost" # from which ip can i receive socket, or receive from all
port = 20000



# 1. Connect with the server
s.connect((ip,port))


try:
    while True:

        message = input("Enter your message:") 
        s.send(message.encode())

        # wait for the answer from the server
        answer = s.recv(1024)

        print(f"[{ip}]  {answer.decode()}")



except:
    print("Something wrong happend!") 

finally:
    s.close()
