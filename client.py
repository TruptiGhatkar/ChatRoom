import socket
from threading import Thread

name = input("Enter your name : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5555))  #Provide server ip address , port number you want to connect
client.send(name.encode()) #Sending client name to server

#For sending and receiving msg at a time thread is used
#Create function for sending msg to other client using thread
def send(client):
    while True:
        #Add f string before sending data for  recognizing client name  who send data
        data = f'{name} : {input("")}' # Enter data for sending to other client (It is in string format)
        client.send(data.encode()) #Encode data into byte format before sending

#Create function for receiving msg from other client using thread
def receive(client):
    while True:
        try:
            data = client.recv(1024).decode()
            print(data)
        except:
            client.close()
            break

thread1 = Thread(target=send, args=(client,))
thread1.start()
thread2 = Thread(target=receive, args=(client,))
thread2.start()
