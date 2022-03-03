
from xmlrpc.server import SimpleXMLRPCServer as Server 


# Define functions
def addieren(x,y):
    return x + y 


def subtrahieren(x,y):
    return x - y 


# Create  a Server with Tuple [IP, PORT]
srv = Server(("127.0.0.1", 40000))

# Register the functions to the server 
srv.register_function(addieren)
srv.register_function(subtrahieren)


# Start the Server 
srv.serve_forever()
