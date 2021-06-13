import socket
import sys

if(len(sys.argv) >1):
   ServerIP = sys.argv[1]
else:
   print("\n\n Run like \n python3 5.4.client.py 192.168.56.103 \n\n")
   exit(1)

s = socket.socket()

PORT = 8889

s.connect((ServerIP, PORT))

print("What file you want to sent?")
filename = input("Name of file:")
print("Filename: " + filename)


file = open(filename, "rb")
SendData = file.read(1024)

while SendData:
    print("\n\n-----Below message is received from server----- \n\n", s.recv(1024).decode("utf-8"))
    s.send(SendData)
    SendData = file.read(1024)


s.close()
