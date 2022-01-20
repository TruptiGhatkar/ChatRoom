import socket
from threading import Thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))   #server ip address , port number

server.listen()
all_clients ={}

def client_thread(client):
    while True:
        try:
            msg = client.recv(1024)  #msg is in byte format #decode is not reguired
            for c in all_clients:
                c.send(msg) # we not decode the msg that's why here encode is not required
        except:
            for c in all_clients:
                if c != client:
                    c.send(f"{name} has left the chat.".encode()) #Inform all the clients that new client is left the chat except that client
            del all_clients[ client ] #Delete the client which is disconnected
            client.close()
            break
            
while True:
    print("Waiting for connection")
    client , address = server.accept()
    print("Connection establish")
    name = client.recv(1024).decode()  # decode client name which is in byte format
    all_clients[client] = name
    
    for c in all_clients:
        if c != client:
            c.send(f"{name} has join the chat.".encode()) #Inform all the client that new client is join the chat except that client

    thread = Thread(target=client_thread, args=(client,))
    thread.start()
    
