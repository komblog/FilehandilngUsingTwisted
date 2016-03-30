import socket

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect(("127.0.0.1", 4000))

command = raw_input("Command : ")
c.sendall(command)

while True:
    reply = c.recv(8100)
    if reply:
        print "Server say :",reply
    else:
        break
