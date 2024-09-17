#Server Moment
import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 34387  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Digit Sum Server Started")
    s.bind((HOST, PORT))
    s.listen()
    print("Listening on TCP", PORT)
    conn, addr = s.accept()
    with conn:
        # print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)

            if not data:
                break
            
            dataDecoded = data.decode()
            print("Recieved string: "+ dataDecoded)

            #is a digit
            if dataDecoded.isdigit():                
                dataSum = 0
                for i in dataDecoded:
                    i = int(i)
                    dataSum += i

                dataDecoded = dataSum
                print("Sending Digit Sum result:", dataDecoded)

                if dataDecoded <= 9:
                    print("\nDigit sum is a single digit, Exiting Server Application")
                
            #Not a digit
            else:
                print("\nInvalid Input, Exiting Server Application")
                dataDecoded = "Not A Number error"   

            
            conn.sendall(str(dataDecoded).encode())
