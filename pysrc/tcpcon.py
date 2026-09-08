import socket

print("Hello world")

CONNECTION_TIMEOUT = 5

host = input("Enter Host IP: ")
try:
    port = int(input("Input port number: "))
except ValueError:
    print("Invalid port number. Please enter an integer.")
    raise SystemExit(1)

if not 1 <= port <= 65535:
    print("Invalid port number. Use a value between 1 and 65535.")
    raise SystemExit(1)

soc = socket.socket()
soc.settimeout(CONNECTION_TIMEOUT)

try:
    soc.connect((host, port))
    banner = soc.recv(1024)
    print(banner.decode('utf-8', errors='ignore'))
except socket.timeout:
    print(f"Connection timed out after {CONNECTION_TIMEOUT} seconds.")
except socket.gaierror:
    print(f"Could not resolve host: {host}")
except ConnectionRefusedError:
    print(f"Connection refused by {host}:{port}.")
except OSError as e:
    print(f"Host unreachable or network error: {e}")
finally:
    soc.close()
