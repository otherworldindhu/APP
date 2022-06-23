#tcp server

import socket
s=socket.socket()
host=socket.gethostname()
port=99
s.bind((host,port))
print("Waiting for connection")
s.listen(5)

while True:
    conn,addr=s.accept()
    print("GOt connection from",addr)
    conn.send("server saying hi")
    conn.close()


