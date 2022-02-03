import server
server_socket = server.conn('192.168.1.5', 9999)
server.frame(server_socket, 0)
