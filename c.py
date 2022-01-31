import client

client_socket = client.conn('192.168.1.5', 9999)

while True:
    data = client.recv(client_socket)
    print(data)