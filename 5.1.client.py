import socket


s = socket.socket()


port = 8888
host = '192.168.56.103'


s.connect(('192.168.56.103', port))


data = s.recv(1024)


s.send(b'Hi saya client, Terima Kasih!')


print(data)


s.close()