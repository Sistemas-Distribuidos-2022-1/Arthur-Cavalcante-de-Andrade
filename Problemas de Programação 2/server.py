from socket import *
from questoes import *
import threading

def handle_client(connectionSocket,addr):
    while True:
        quest = int(connectionSocket.recv(1024).decode())

        print('Entrando na opção', quest, '...')
        if quest == 0:
            print('Conexão encerrada')
            connectionSocket.close()
            exit()
        elif quest == 1: q1(connectionSocket)
        elif quest == 2: q2(connectionSocket)
        elif quest == 3: q3(connectionSocket)
        elif quest == 4: q4(connectionSocket)
        elif quest == 5: q5(connectionSocket)
        elif quest == 6: q6(connectionSocket)
        elif quest == 7: q7(connectionSocket)
        elif quest == 8: q8(connectionSocket)
        elif quest == 9: q9(connectionSocket)
        else:
            print('Opção não existente')
            connectionSocket.send('404 not found'.encode())
            continue


if __name__ == '__main__':
    serverPort = 8000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)

    all_threads = []
    print('Servidor pronto')
    try:
        while True:
            connectionSocket, addr = serverSocket.accept()

            t = threading.Thread(target=handle_client, args=(connectionSocket,addr))
            t.start()
            all_threads.append(t)

    except KeyboardInterrupt:
        print("Stopped by Ctrl+C")
    finally:
        if serverSocket:
            serverSocket.close()
        for t in all_threads:
            t.join()