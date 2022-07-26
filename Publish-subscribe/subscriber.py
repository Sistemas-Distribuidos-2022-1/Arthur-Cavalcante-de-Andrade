import zmq
import questoes

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://localhost:8000"
s.connect(p)

quest = int(input("Número da questão (1-9): "))
if quest not in [1,2,3,4,5,6,7,8,9]:
    print("Valor incorreto")
    exit()

s.setsockopt_string(zmq.SUBSCRIBE, "Q"+str(quest))
print('Inscrito na Questão '+str(quest))

if quest == 1:
    while True:
        _, nome, cargo, sal = s.recv().decode().split()
        nome = nome.replace('[','').replace(']','').replace('\'','')
        cargo = cargo.replace('[','').replace(']','').replace('\'','')
        questoes.q1(nome, cargo, float(sal))

elif quest == 2:
    while True:
        _, nome, sexo, idade = s.recv().decode().split()
        nome = nome.replace('[','').replace(']','').replace('\'','')
        questoes.q2(nome, sexo, int(idade))

elif quest == 3:
    while True:
        _, n1, n2, n3 = s.recv().decode().split()
        questoes.q3(float(n1), float(n2), float(n3))

elif quest == 4:
    while True:
        _, altura, sexo = s.recv().decode().split()
        questoes.q4(float(altura), sexo)

elif quest == 5:
    while True:
        _, idade = s.recv().decode().split()
        questoes.q5(int(idade))

elif quest == 6:
    while True:
        _, nome, nivel, sal, dependentes = s.recv().decode().split()
        nome = nome.replace('[','').replace(']','').replace('\'','')
        nivel = nivel.replace('[','').replace(']','').replace('\'','')
        questoes.q6(nome, nivel, float(sal), float(dependentes))

elif quest == 7:
    while True:
        _, idade, tempo = s.recv().decode().split()
        questoes.q7(int(idade), int(tempo))

elif quest == 8:
    while True:
        _, saldo = s.recv().decode().split()
        questoes.q8(int(saldo))

else:
    while True:
        _, valor, naipe = s.recv().decode().split()
        questoes.q9(int(valor), int(naipe))