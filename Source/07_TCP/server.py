
import socket

print("Server Side TCP")
print("~" * 30)

# Create Socket
# AF_INET: IPV4
# SOCK_STREAM : TCP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ip = "" # from which ip can i receive socket, or receive from all
port = 20000


s.bind((ip,port))
s.listen()

try:
    # Accept the connection from the client
    comm, add = s.accept()

    while True:
        data = comm.recv(1024)  # waits for any messages 1024 Data Buffer Size

        if not data: # if not data then break loop
            comm.close()
            break

        print(f"[{add[0]}]    {data.decode()}")

        response_text = input("Answer: ")
        comm.send(response_text.encode())

except:
    print("Something wrong happend!") 

finally:
    s.close()
