from xmlrpc.client import ServerProxy 



# Create the Client with the IP and Port of the Server
cli = ServerProxy("http://127.0.0.1:40000")


# Call the Remote Function/Procedure
print(cli.addieren(50,5))
