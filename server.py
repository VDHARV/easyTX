import socket

def conn(host_ip, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 65535)
    print('Socket Created ')
    server_socket.bind((host_ip, port))
    print('Waiting for conn: ')


def data(server_socket):
    while True:
        msg, addr = server_socket.recvfrom(65535)
        print('GOT: ', addr)
        # Data send 
        # for i in range(0, 10000):
        #     message = str(i)
        #     message = message.encode('utf-8')
        #     server_socket.sendto(message, addr)