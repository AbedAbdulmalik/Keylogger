import socket

server_ip = "0.0.0.0"
server_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_ip, server_port))
server.listen(5)

print(f"[*] Listening on {server_ip}:{server_port}")

while True:
    client_socket, addr = server.accept()
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
    request = client_socket.recv(1024)
    print(f"[*] Received: {request.decode('utf-8')}")
    client_socket.close()
