from socket import *

serverName = 'localhost'
serverPort = 8000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    quest = input('De 1 a 9, qual questão você deseja testar? (0 encerra o WebSocket)\n')
    clientSocket.send(quest.encode())
    if quest == '0':
        print('Conexão encerrada')
        clientSocket.close()
        break

    resp = clientSocket.recv(1024).decode()
    if resp == '404 not found':
        print(resp)
        continue

    while resp != 'processing':
        print(resp)
        clientSocket.send(input().encode())
        resp = clientSocket.recv(1024).decode()

    print(clientSocket.recv(1024).decode(), '\n')
