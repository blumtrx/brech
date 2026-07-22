import socket

print("Hello world")

soc = socket.socket()

host = input("Enter Host IP: ")
port = int(input("Input port number: "))

try:
    soc.connect((host, port))
    banner = soc.recv(1024)
    print(banner.decode('utf-8', errors='ignore'))
    
except Exception as e:
    print(f"Connection error: {e}")
    
finally:
    soc.close()
