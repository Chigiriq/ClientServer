#Client, its exactly like a server but not

import socket

# HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 34387  # The port used by the server

HOST = input("Server IP>> ")
PORT = int(input("Server PORT>> "))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Digit Sum Client Started")
    
    sendValue = input("Digit Sum starting string>> ")
    
    while True:
        #Number value end condition
        if (len(sendValue)) == 1:
            sendValue = "a single digit result"
            break
        
        print("Sending", sendValue, "to digit sum server")
        s.sendall(sendValue.encode())
        data = s.recv(1024)
        print("Recieved Digit Sum result: " + data.decode())

        #Error value end condition
        if not (data.decode().isdigit()):
            sendValue = data.decode()
            break
        
        sendValue = data.decode()


print("\nServer returned " + sendValue + ", Exiting Client Application")