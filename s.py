import server_data

server_socket = server_data.conn('192.168.1.5', 9999)

while True:
    addr = server_data.address(server_socket)
    for i in range(0, 10000):
        message = str(i)
        message = message.encode('utf-8')
        server_data.send(server_socket, message, addr)