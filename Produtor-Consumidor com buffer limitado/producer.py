import rpyc
import time, random

try:
    conn = rpyc.connect(None, 12345)
except ConnectionRefusedError:
    print('Buffer Offline')
    exit()

while True:
    try:
        id = random.randint(1,1000)
        conn.root.produce(id)
        print('Produced {}'.format(id))
        time.sleep(2)
    except EOFError:
        print('Buffer Disconnected')
        exit()