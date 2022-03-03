import socket

print("Server Side UDP")
print("~" * 30)


# Create Socket
# AF_INET: IPV4
# SOCK_DGRAM : UDP



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = "" # from which ip can i receive socket, or receive from all
port = 10000


try:
    s.bind((ip,port))  # tuple of (ip, port)

    while True:
        data, add = s.recvfrom(1024) # waits for any messages
        print("Data:", data)
        print("Address:", add)

        print(f"[{add[0]}]    {data.decode()}")

except:
    print("Something wrong happend!") 

finally:
    s.close()