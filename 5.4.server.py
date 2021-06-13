import socket

s = socket.socket()

PORT = 8889
print("\nServer listening to port :", PORT, "\n")

s.bind(('', PORT))

s.listen(10)

file = open("notapertama.txt", "wb")
print("\n Copied file notapertama.txt at server side\n")

while True:
    conn, addr = s.accept()


    msg ="\n\n-----\n Hi Client[IP address: "+ addr[0] + "], \n**Welcome to the Server** \n -Server\n----\n \n\n"
    conn.send(msg.encode())

    RecvData = conn.recv(1024)
    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(1024)

    file.close()
    print("\n File has been coppied successfully \n")

    conn.close()
    print("\nServer closed the connection \n")

    break
