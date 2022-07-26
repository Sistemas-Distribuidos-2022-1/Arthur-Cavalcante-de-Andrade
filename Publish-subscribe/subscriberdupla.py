#Implementado durante a aula para o publisher em Golang do William
#O subscriber para o publisher.py é o subscriber.py

import zmq
import questoes

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://192.168.6.160:5012"
s.connect(p)

quest = int(input("Número da questão (1-9): "))
if quest not in [1,2,3,4,5,6,7,8,9]:
    print("Valor incorreto")
    exit()

s.setsockopt_string(zmq.SUBSCRIBE, "Q"+str(quest))
print('Inscrito na Questão '+str(quest))

if quest == 1:
    while True:
        s.recv().decode()
        nome = s.recv().decode().upper()
        cargo = s.recv().decode().upper()
        sal = float(s.recv().decode())
        questoes.q1(nome, cargo, sal)

elif quest == 2:
    while True:
        s.recv().decode()
        nome = s.recv().decode().upper()
        sexo = s.recv().decode().upper()
        idade = int(s.recv().decode())
        questoes.q2(nome, sexo, idade)

elif quest == 3:
    while True:
        s.recv().decode()
        n1 = float(s.recv().decode())
        n2 = float(s.recv().decode())
        n3 = float(s.recv().decode())
        questoes.q3(n1, n2, n3)

elif quest == 4:
    while True:
        s.recv().decode()
        altura = float(s.recv().decode())
        sexo = s.recv().decode()
        questoes.q4(altura, sexo)

elif quest == 5:
    while True:
        s.recv().decode()
        idade = int(s.recv().decode())
        questoes.q5(idade)

elif quest == 6:
    while True:
        s.recv().decode()
        nome = s.recv().decode()
        nivel = s.recv().decode()
        sal = float(s.recv().decode())
        dependentes = int(s.recv().decode())
        questoes.q6(nome, nivel, sal, dependentes)

elif quest == 7:
    while True:
        s.recv().decode()
        idade = int(s.recv().decode())
        tempo = int(s.recv().decode())
        questoes.q7(idade, tempo)

elif quest == 8:
    while True:
        s.recv().decode()
        saldo = int(s.recv().decode())
        questoes.q8(saldo)

else:
    while True:
        s.recv().decode()
        valor = int(s.recv().decode())
        naipe = int(s.recv().decode())
        questoes.q9(valor, naipe)