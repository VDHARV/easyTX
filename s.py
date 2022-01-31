import server

server_socket = server.conn('192.168.1.5', 9999)

while True:
    addr = server.address(server_socket)
    for i in range(0, 10000):
        message = str(i)
        message = message.encode('utf-8')
        server.send(server_socket, message, addr)