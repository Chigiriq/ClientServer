#Server Moment
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 34387  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            data = data.decode()

            if not data:
                break

            if data.isdigit():
                print("Recieved string "+ str(data))
                
                for i in str(data):
                    sum += int(i)

                data = sum
                print("Sending Digit Sum result", data)
                

            else:
                print("Invalid Input, Exiting Server Application")
                data = "Not A Number error, Exiting Client Application"   

            
            conn.sendall(data.encode())