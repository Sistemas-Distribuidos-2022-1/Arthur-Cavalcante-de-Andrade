import rpyc
import threading

class BufferService(rpyc.Service):
    def exposed_produce(self, id):
        producer.acquire()
        buffer.append(id)
        if consumer.locked(): consumer.release()
        if len(buffer) < 10: producer.release()
        print("Produced {}, buffer length = {}".format(id, len(buffer)))

    def exposed_consume(self):
        consumer.acquire()
        id = buffer.pop(0)
        if producer.locked(): producer.release()
        if len(buffer) > 0: consumer.release()
        print("Consumed {}, buffer length = {}".format(id, len(buffer)))
        return id

while True:
    try:
        limit = int(input('Insert buffer limit: '))
    except ValueError:
        print('Wrong type inserted')
        continue
    break

buffer = []
producer = threading.Lock()
consumer = threading.Lock()
consumer.acquire()

server = rpyc.ThreadedServer(BufferService, port=12345)
print("Buffer Online")
server.start()