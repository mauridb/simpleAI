import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 8000))
serversocket.listen(5)

while True:
    (clientsocket, address) = serversocket.accept()
    print clientsocket, address
    ct = client_thread(clientsocket)
    ct.run()
