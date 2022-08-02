import rpyc
import time

try:
    conn = rpyc.connect(None, 12345)
except ConnectionRefusedError:
    print('Buffer Offline')
    exit()

while True:
    try:
        id = conn.root.consume()
        print('Consumed {}'.format(id))
        time.sleep(3)
    except EOFError:
        print('Buffer Disconnected')
        exit()