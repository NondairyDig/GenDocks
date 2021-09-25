import socket
import time

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(content)
    i = 1
    while True:
        data = s.recv(1024)
        if data == b"":
            break
        print("Received:", repr(data))
        if i == 1:
            time.sleep(0.5)
            s.send(b'28')
        i = i + 1
    print("Connection closed.")
    s.close()

netcat("pwn-2021.duc.tf", 31905, b"")