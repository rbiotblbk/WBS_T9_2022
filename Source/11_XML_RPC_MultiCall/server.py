from xmlrpc.server import SimpleXMLRPCServer 


def multiply(x, y):
    return x * y 


def add(x, y):
    return x + y 


server = SimpleXMLRPCServer(("localhost", 50000))

server.register_multicall_functions() 


server.register_function(add, "add")
server.register_function(multiply, "multiply")

print("Server is On and Listening.....")


server.serve_forever()


