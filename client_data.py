import cv2
import client
import numpy as np
client_socket = client.conn('192.168.1.5', 9999)
while True:
    frame = client.frame(client_socket)
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
