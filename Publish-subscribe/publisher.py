import zmq
import time
import publicacoes

context = zmq.Context()
s = context.socket(zmq.PUB)
p = "tcp://*:8000"
s.bind(p)

while True:
    time.sleep(2)
    publicacoes.q1(s)
    publicacoes.q2(s)
    publicacoes.q3(s)
    publicacoes.q4(s)
    publicacoes.q5(s)
    publicacoes.q6(s)
    publicacoes.q7(s)
    publicacoes.q8(s)
    publicacoes.q9(s)