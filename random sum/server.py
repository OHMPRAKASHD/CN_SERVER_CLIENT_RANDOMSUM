import socket
import random

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f'Server listening on {HOST}:{PORT}')

# Accept incoming connections
client_socket, address = server_socket.accept()

print(f'Connected by {address}')

# Generate 10 random numbers and calculate the sum
numbers = [random.randint(1, 10) for _ in range(10)]
sum_numbers = sum(numbers)

# Print the random numbers and the sum
print(f'Random numbers: {numbers}')

# Send the sum to the client
client_socket.send(str(sum_numbers).encode())

# Close the socket
client_socket.close()
server_socket.close()

