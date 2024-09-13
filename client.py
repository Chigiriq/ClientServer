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
    
    sendNumber = input("Digit Sum starting string: ")
    
    while (len(sendNumber) > 10):
        print("Sending", sendNumber, "to digit sum server")
        s.sendall(sendNumber.encode())
        data = s.recv(1024)
        print("Recieved Digit Sum result: " + data.decode())
        sendNumber = data.decode()


print(f"Server returned {sendNumber}")

