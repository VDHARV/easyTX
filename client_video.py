import client_data

client_socket = client_data.conn('192.168.1.5', 9999)

while True:
    data = client_data.recv(client_socket)
    print(data)