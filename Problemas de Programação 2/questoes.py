def q1(connectionSocket):
    connectionSocket.send('Nome:'.encode())
    nome = connectionSocket.recv(1024).decode()

    connectionSocket.send('Cargo:'.encode())
    cargo = (connectionSocket.recv(1024).decode()).upper()
    while cargo != 'OPERADOR' and cargo != 'PROGRAMADOR':
        connectionSocket.send('Cargo incorreto, somente \'OPERADOR\' e \'PROGRAMADOR\'. Informe novamente:'.encode())
        cargo = (connectionSocket.recv(1024).decode()).upper()

    connectionSocket.send('Salário:'.encode())
    sal = float(connectionSocket.recv(1024).decode())

    connectionSocket.send('processing'.encode())
    if cargo == 'OPERADOR':
        sal = sal*1.2
    else:
        sal = sal*1.18

    connectionSocket.send(('\nNome: {} \nSalário reajustado: {}'.format(nome, sal)).encode())

    return()


def q2(connectionSocket):
    connectionSocket.send('Nome:'.encode())
    nome = connectionSocket.recv(1024).decode()

    connectionSocket.send('Sexo:'.encode())
    sexo = (connectionSocket.recv(1024).decode()).upper()
    while sexo != 'MASCULINO' and sexo != 'FEMININO':
        connectionSocket.send('Sexo incorreto, somente \'MASCULINO\' e \'FEMININO\'. Informe novamente:'.encode())
        sexo = (connectionSocket.recv(1024).decode()).upper()

    connectionSocket.send('Idade:'.encode())
    idade = int(connectionSocket.recv(1024).decode())

    connectionSocket.send('processing'.encode())
    if (sexo == 'MASCULINO' and idade >= 18) or (sexo == 'FEMININO' and idade >= 21):
        connectionSocket.send(('{} já atingiu a maioridade'.format(nome)).encode())
    else:
        connectionSocket.send(('{} ainda não atingiu a maioridade'.format(nome)).encode())

    return()


def q3(connectionSocket):
    connectionSocket.send('Nota N1:'.encode())
    n1 = float(connectionSocket.recv(1024).decode())
    connectionSocket.send('Nota N2:'.encode())
    n2 = float(connectionSocket.recv(1024).decode())
    connectionSocket.send('Nota N3:'.encode())
    n3 = float(connectionSocket.recv(1024).decode())

    connectionSocket.send('processing'.encode())
    m = (n1+n2)/2
    if (m >= 7) or (m > 3 and (m+n3)/2 >= 5):
        connectionSocket.send('O aluno foi aprovado'.encode())
    else: connectionSocket.send('O aluno foi reprovado'.encode())

    return()


def q4(connectionSocket):
    connectionSocket.send('Altura:'.encode())
    altura = float(connectionSocket.recv(1024).decode())

    connectionSocket.send('Sexo:'.encode())
    sexo = (connectionSocket.recv(1024).decode()).upper()
    while sexo != 'MASCULINO' and sexo != 'FEMININO':
        connectionSocket.send('Sexo incorreto, somente \'MASCULINO\' e \'FEMININO\'. Informe novamente:'.encode())
        sexo = (connectionSocket.recv(1024).decode()).upper()

    connectionSocket.send('processing'.encode())
    if sexo == 'MASCULINO':
        ideal = (72.7 * altura) - 58
    else: ideal = (62.1 * altura) - 44.7

    connectionSocket.send(('Peso Ideal = {}'.format(ideal)).encode())

    return()


def q5(connectionSocket):
    connectionSocket.send('Idade:'.encode())
    idade = int(connectionSocket.recv(1024).decode())

    connectionSocket.send('processing'.encode())
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

    return()


def q6(connectionSocket):
    connectionSocket.send('Nome:'.encode())
    nome = connectionSocket.recv(1024).decode()

    connectionSocket.send('Nível:'.encode())
    nivel = (connectionSocket.recv(1024).decode()).upper()
    while nivel != 'A' and nivel != 'B' and nivel != 'C' and nivel != 'D':
        connectionSocket.send('Nível incorreto, somente \'A\', \'B\', \'C\' e \'D\'. Informe novamente:'.encode())
        nivel = (connectionSocket.recv(1024).decode()).upper()

    connectionSocket.send('Salário bruto:'.encode())
    sal = float(connectionSocket.recv(1024).decode())
    connectionSocket.send('Número de dependentes:'.encode())
    dependentes = int(connectionSocket.recv(1024).decode())

    connectionSocket.send('processing'.encode())
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

    return()


def q7(connectionSocket):
    connectionSocket.send('Idade:'.encode())
    idade = int(connectionSocket.recv(1024).decode())
    connectionSocket.send('Tempo de serviço (em anos):'.encode())
    tempo = int(connectionSocket.recv(1024).decode())

    connectionSocket.send('processing'.encode())
    '''
    O enunciado dessa questão afirma que TODAS as condições devem ser satisfeitas (AND),
    mas isso implica que a terceira condição seria desnecessária.
    Dessa forma, considerei cada condição de forma idependente (OR).
    '''
    if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
        connectionSocket.send('O funcionário já pode se aposentar'.encode())
    else:
        connectionSocket.send('O funcionário não pode se aposentar'.encode())

    return()


def q8(connectionSocket):
    connectionSocket.send('Saldo médio:'.encode())
    saldo = int(connectionSocket.recv(1024).decode())
    while saldo < 0:
        connectionSocket.send('Somente saldo positivo. Informe novamente:'.encode())
        saldo = int(connectionSocket.recv(1024).decode())

    connectionSocket.send('processing'.encode())
    if saldo <= 200:
        connectionSocket.send(('Saldo médio: {}\nValor do Crédito {}'.format(saldo, 0)).encode())
    elif saldo <= 400:
        connectionSocket.send(('Saldo médio: {}\nValor do Crédito {}'.format(saldo, saldo*0.2)).encode())
    elif saldo <= 600:
        connectionSocket.send(('Saldo médio: {}\nValor do Crédito {}'.format(saldo, saldo*0.3)).encode())
    else:
        connectionSocket.send(('Saldo médio: {}\nValor do Crédito {}'.format(saldo, saldo*0.4)).encode())

    return()


def q9(connectionSocket):
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

    connectionSocket.send('Valor:'.encode())
    valor = int(connectionSocket.recv(1024).decode())
    while valor < 1 or valor >13:
        connectionSocket.send('Valor incorreto, somente de 1 a 13. Informe novamente:'.encode())
        valor = int(connectionSocket.recv(1024).decode())

    connectionSocket.send('Naipe:'.encode())
    naipe = int(connectionSocket.recv(1024).decode())
    while naipe < 1 or naipe > 4:
        connectionSocket.send('Naipe incorreto, somente de 1 a 4. Informe novamente:'.encode())
        naipe = int(connectionSocket.recv(1024).decode())

    connectionSocket.send('processing'.encode())
    carta = Carta(valor, naipe)
    connectionSocket.send(carta.extenso().encode())

    return()