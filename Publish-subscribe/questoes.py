def q1(nome, cargo, sal):
    if cargo != 'OPERADOR' and cargo != 'PROGRAMADOR':
        print('Cargo incorreto, somente \'OPERADOR\' e \'PROGRAMADOR\'')
    else:
        if cargo == 'OPERADOR':
            sal = sal*1.2
        else:
            sal = sal*1.18

        print('Nome: {} \nSalário reajustado: {}'.format(nome, sal))


def q2(nome, sexo, idade):
    if sexo != 'MASCULINO' and sexo != 'FEMININO':
        print('Sexo incorreto, somente \'MASCULINO\' e \'FEMININO\'')
    else:
        if (sexo == 'MASCULINO' and idade >= 18) or (sexo == 'FEMININO' and idade >= 21):
            print('{} já atingiu a maioridade'.format(nome))
        else:
            print('{} ainda não atingiu a maioridade'.format(nome))


def q3(n1, n2, n3):
    m = (n1+n2)/2
    if (m >= 7) or (m > 3 and (m+n3)/2 >= 5):
        print('O aluno foi aprovado')
    else: print('O aluno foi reprovado')
    return()


def q4(altura, sexo):
    if sexo != 'MASCULINO' and sexo != 'FEMININO':
        print('Sexo incorreto, somente \'MASCULINO\' e \'FEMININO\'')
    else:
        if sexo == 'MASCULINO':
            ideal = (72.7 * altura) - 58
        else: ideal = (62.1 * altura) - 44.7
        print('Peso Ideal = {}'.format(ideal))


def q5(idade):
    if idade < 5:
        print('Sem classificação')
    elif idade <= 7:
        print('Infantil A')
    elif idade <= 10:
        print('Infantil B')
    elif idade <= 13:
        print('Juvenil A')
    elif idade <= 17:
        print('Juvenil B')
    else:
        print('Adulto')


def q6(nome, nivel, sal, dependentes):
    if nivel != 'A' and nivel != 'B' and nivel != 'C' and nivel != 'D':
        print('Nível incorreto, somente \'A\', \'B\', \'C\' e \'D\'')
    else:
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

        print('Nome: {}\nNível: {}\nSalário líquido: {}'.format(nome, nivel, sal))


def q7(idade, tempo):
    '''
    O enunciado dessa questão afirma que TODAS as condições devem ser satisfeitas (AND),
    mas isso implica que a terceira condição seria desnecessária.
    Dessa forma, considerei cada condição de forma idependente (OR).
    '''
    if idade >= 65 or tempo >= 30 or (idade >= 60 and tempo >= 25):
        print('O funcionário já pode se aposentar')
    else:
        print('O funcionário não pode se aposentar')


def q8(saldo):
    if saldo < 0:
        print('Somente saldo positivo')
    else:
        if saldo <= 200:
            print('Saldo médio: {}\nValor do Crédito {}')
        elif saldo <= 400:
            print('Saldo médio: {}\nValor do Crédito {}'.format(saldo, saldo*0.2))
        elif saldo <= 600:
            print('Saldo médio: {}\nValor do Crédito {}'.format(saldo, saldo*0.3))
        else:
            print('Saldo médio: {}\nValor do Crédito {}'.format(saldo, saldo*0.4))


def q9(valor, naipe):
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

    if valor < 1 or valor >13:
        print('Valor incorreto, somente de 1 a 13')

    elif naipe < 1 or naipe > 4:
        print('Naipe incorreto, somente de 1 a 4')
    else:
        carta = Carta(valor, naipe)
        print(carta.extenso())