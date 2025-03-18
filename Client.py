import socket
s = socket.socket()
s.connect(('localhost', 8000))
while True:
    # Receive data from server
    data = s.recv(1024).decode()
    if not data:
        break
    print("Received from Server:", data)
    s.send("Acknowledgement Received".encode())

s.close()