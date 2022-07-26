import random

nome = ['Arthur', 'Sérgio', 'Gabriel', 'Lays', 'William', 'Cristinny']
sexo = {'[\'Arthur\']':'MASCULINO', '[\'Sérgio\']':'MASCULINO', '[\'Gabriel\']':'MASCULINO',
        '[\'Lays\']':'FEMININO', '[\'William\']':'MASCULINO', '[\'Cristinny\']':'FEMININO'}

def q1(s):
    a = str(random.sample(nome, 1))
    b = str(random.sample(['OPERADOR', 'PROGRAMADOR','OUTRO'], 1))
    c = str(random.uniform(500, 5000))
    s.send_string('Q1 '+a+' '+b+' '+c)

def q2(s):
    a = str(random.sample(nome,1))
    b = str(sexo[a])
    c = str(random.randint(10,60))
    s.send_string('Q2 '+a+' '+b+' '+c)

def q3(s):
    a = str(random.randint(0,10))
    b = str(random.randint(0,10))
    c = str(random.randint(0,10))
    s.send_string('Q3 '+a+' '+b+' '+c)

def q4(s):
    a = str(random.uniform(1,2))
    b = str(sexo[str(random.sample(nome,1))])
    s.send_string('Q4 '+a+' '+b)

def q5(s):
    a = str(random.randint(0,25))
    s.send_string('Q5 '+a)

def q6(s):
    a = str(random.sample(nome,1))
    b = str(random.sample(['A','B','C','D','E'],1))
    c = str(random.uniform(500,5000))
    d = str(random.randint(0,5))
    s.send_string('Q6 '+a+' '+b+' '+c+' '+d)

def q7(s):
    a = str(random.randint(18,80))
    b = str(random.randint(0,50))
    s.send_string('Q7 '+a+' '+b)

def q8(s):
    a = str(random.randint(0,5000))
    s.send_string('Q8 '+a)

def q9(s):
    a = str(random.randint(0,13))
    b = str(random.randint(0,4))
    s.send_string('Q9 '+a+' '+b)