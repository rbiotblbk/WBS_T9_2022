import xmlrpc.client 


proxy = xmlrpc.client.ServerProxy("http://localhost:50000")
multicall = xmlrpc.client.MultiCall(proxy) 

# Assign the required functions with its variables
multicall.add(6,4)
multicall.multiply(6,4)

# Call the bundled functions and get the result 
results = multicall() # Iterator 

# Convert the iterator to a tuple
print(tuple(results))

# Convert the iterator to a tuple
results = tuple(results)

# Print the Output results
print(f"Add: {results[0]} , Multiply:{results[1]}")