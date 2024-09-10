#Client, its exactly like a server but not

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 34387  # The port used by the server
# HOST = input("Server Ip")
# PORT = input("Server Port")

print(HOST)
print(PORT)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # s.sendall(b"Hello, world")
    sendNumber = input("Digit Sum starting string: ")
    s.sendall(sendNumber.encode())
 
    data = s.recv(1024)


# print(f"Received {data!r}")
print(f"Server returned {data.decode()}")
