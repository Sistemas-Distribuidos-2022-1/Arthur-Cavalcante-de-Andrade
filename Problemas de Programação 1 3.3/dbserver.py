from socket import *
from time import *
import threading
import io

def handle_client(connectionSocket, addr):
    quest = int(connectionSocket.recv(1024).decode())
    db = (io.open("dados.txt", "r")).read()
    search = db[db.find('Q' + str(quest)) + 3:db.find('Q' + str(quest+1))].upper().replace('\n', ',').split(',')
    print(search)
    param = connectionSocket.recv(1024).decode()

    if param in search:
        if quest in [5,8]:
            connectionSocket.send(search[search.index(param) + 1].encode())
        elif quest in [1,2,4,7,9]:
            connectionSocket.send(search[search.index(param) + 1].encode())
            sleep(0.1)
            connectionSocket.send(search[search.index(param) + 2].encode())
        elif quest in [3,6]:
            connectionSocket.send(search[search.index(param) + 1].encode())
            sleep(0.1)
            connectionSocket.send(search[search.index(param) + 2].encode())
            sleep(0.1)
            connectionSocket.send(search[search.index(param) + 3].encode())
    else:
        connectionSocket.send('NONE'.encode())


if __name__ == '__main__':
    serverPort = 8080
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)

    all_threads = []
    print('Servidor pronto')
    try:
        while True:
            connectionSocket, addr = serverSocket.accept()

            t = threading.Thread(target=handle_client, args=(connectionSocket, addr))
            t.start()
            all_threads.append(t)
    except KeyboardInterrupt:
        print("Stopped by Ctrl+C")
    finally:
        if serverSocket:
            serverSocket.close()
        for t in all_threads:
            t.join()