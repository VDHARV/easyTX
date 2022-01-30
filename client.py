from http import client
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65535)
print('Socket Created ')

host_ip = '192.168.1.5'
port = 9999

host_name = socket.gethostname()
print(host_ip, host_name)
message = b'Hello'
client_socket.sendto(message, (host_ip, port))

while True:
    packet, _ = client_socket.recvfrom(65535)
    data = packet.decode('utf-8')
    print(data)