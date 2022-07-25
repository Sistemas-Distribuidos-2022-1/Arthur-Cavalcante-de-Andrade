from time import *
def q1(connectionSocket,dbSocket,nome):

    cargo = dbSocket.recv(1024).decode()
    if cargo != 'NONE':
        cargo.upper()
        sal = float(dbSocket.recv(1024).decode())

        if cargo == 'OPERADOR':
            sal = sal*1.2
        else:
            sal = sal*1.18

        connectionSocket.send(('Nome: {} \nSalário reajustado: {}'.format(nome, sal)).encode())
    else:
        connectionSocket.send('Dado inexistente'.encode())

    return()


def q2(connectionSocket,dbSocket,nome):

    sexo = (dbSocket.recv(1024).decode()).upper()
    if sexo != 'NONE':
        idade = int(dbSocket.recv(1024).decode())
        if (sexo == 'MASCULINO' and idade >= 18) or (sexo == 'FEMININO' and idade >= 21):
            connectionSocket.send(('{} já atingiu a maioridade'.format(nome)).encode())
        else:
            connectionSocket.send(('{} ainda não atingiu a maioridade'.format(nome)).encode())
    else:
        connectionSocket.send('Dado inexistente'.encode())

    return()


def q3(connectionSocket,dbSocket,nome):

    n1 = dbSocket.recv(1024).decode()
    if n1 != 'NONE':
        n1 = float(n1)
        n2 = float(dbSocket.recv(1024).decode())
        n3 = float(dbSocket.recv(1024).decode())

        m = (n1+n2)/2
        if (m >= 7) or (m > 3 and (m+n3)/2 >= 5):
            connectionSocket.send('O aluno foi aprovado'.encode())
        else: connectionSocket.send('O aluno foi reprovado'.encode())
    else:
        connectionSocket.send('Dado inexistente'.encode())

    return()


def q4(connectionSocket,dbSocket):

    altura = dbSocket.recv(1024).decode()
    if altura != 'NONE':
        altura = float(altura)
        sexo = (dbSocket.recv(1024).decode()).upper()

        if sexo == 'MASCULINO':
            ideal = (72.7 * altura) - 58
        else: ideal = (62.1 * altura) - 44.7

        connectionSocket.send(('Peso Ideal = {}'.format(ideal)).encode())
    else:
        connectionSocket.send('Dado inexistente'.encode())

    return()


def q5(connectionSocket,dbSocket):

    idade = dbSocket.recv(1024).decode()
    if idade != 'NONE':
        idade = int(idade)

        if idade < 5:
            connectionSocket.send('Sem classificação'.encode())
        elif idade <= 7:
            connectionSocket.send('Infantil A'.encode())
        elif idade <= 10:
            connectionSocket.send('Infantil B'.encode())
        elif idade <= 13:
            connectionSocket.send('Juvenil A'.encode())
        elif idade <= 17:
            connectionSocket.send('Juvenil B'.encode())
        else:
            connectionSocket.send('Adulto'.encode())
    else:
        connectionSocket.send('Dado inexistente'.encode())

    return()


def q6(connectionSocket,dbSocket,nome):

    nivel = (dbSocket.recv(1024).decode()).upper()
    if nivel != 'NONE':
        sal = float(dbSocket.recv(1024).decode())
        dependentes = int(dbSocket.recv(1024).decode())

        if dependentes <= 0:
            if nivel == 'A':
                sal = sal*(1-0.03)
            elif nivel == 'B':
                sal = sal*(1-0.05)
            elif nivel == 'C':
                sal = sal*(1-0.08)
            else:
                sal = sal*(1-0.1)
        else:
            if nivel == 'A':
                sal = sal*(1-0.08)
            elif nivel == 'B':
                sal = sal*(1-0.10)
            elif nivel == 'C':
                sal = sal*(1-0.15)
            else:
                sal = sal*(1-0.17)

        connectionSocket.send(('Nome: {}\nNível: {}\nSalário líquido: {}'.format(nome, nivel, sal)).encode())
    else:
        connectionSocket.send('Dado inexistente'.encode())

    return()


def q7(connectionSocket,dbSocket):

    idade = dbSocket.recv(1024).decode()
    if idade != 'NONE':
        idade = int(idade)
        tempo = int(dbSocket.recv(1024).decode())

        '''
        O enunciado dessa questão afirma que TODAS as condições devem ser satisfeitas (AND),
        mas isso implica que a terceira condição seria desnecessária.
        Dessa forma, considerei cada condição de forma idependente (OR).
        '''
        if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
            connectionSocket.send('O funcionário já pode se aposentar'.encode())
        else:
            connectionSocket.send('O funcionário não pode se aposentar'.encode())
    else:
        connectionSocket.send('Dado inexistente'.encode())

    return()


def q8(connectionSocket,dbSocket):

    saldo = dbSocket.recv(1024).decode()
    if saldo != 'NONE':
        saldo = int(saldo)

        if saldo <= 200:
            connectionSocket.send(('Saldo médio: {}\nValor do Crédito {}'.format(saldo, 0)).encode())
        elif saldo <= 400:
            connectionSocket.send(('Saldo médio: {}\nValor do Crédito {}'.format(saldo, saldo*0.2)).encode())
        elif saldo <= 600:
            connectionSocket.send(('Saldo médio: {}\nValor do Crédito {}'.format(saldo, saldo*0.3)).encode())
        else:
            connectionSocket.send(('Saldo médio: {}\nValor do Crédito {}'.format(saldo, saldo*0.4)).encode())
    else:
        connectionSocket.send('Dado inexistente'.encode())

    return()


def q9(connectionSocket,dbSocket):
    dbSocket.send('9'.encode())
    class Carta:
        def __init__(self, valor, naipe):
            self.valor = int(valor)
            self.naipe = int(naipe)

        def extenso(self):
            valores = {1: 'Ás', 2: 'Dois', 3: 'Três', 4: 'Quatro',
            5: 'Cinco', 6: 'Seis', 7: 'Sete', 8: 'Oito', 9: 'Nove',
            10: 'Dez', 11: 'Valete', 12: 'Dama', 13: 'Rei'}
            naipes = {1: 'Ouros', 2: 'Paus',3: 'Copas',4: 'Espadas'}

            nome = valores[self.valor]+' de '+naipes[self.naipe]
            return(nome)

    valor = dbSocket.recv(1024).decode()
    if valor != 'NONE':
        valor = int(valor)
        naipe = int(dbSocket.recv(1024).decode())

        carta = Carta(valor, naipe)
        connectionSocket.send(carta.extenso().encode())
    else:
        connectionSocket.send('Dado inexistente'.encode())

    return()