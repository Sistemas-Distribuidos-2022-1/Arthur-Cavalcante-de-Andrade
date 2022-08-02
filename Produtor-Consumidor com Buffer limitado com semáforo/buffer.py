import rpyc
import threading

class BufferService(rpyc.Service):
    def exposed_produce(self, id):
        full.acquire()
        buffer.append(id)
        empty.release()
        print("Produced {}, buffer length = {}".format(id, len(buffer)))

    def exposed_consume(self):
        empty.acquire()
        id = buffer.pop(0)
        full.release()
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
full = threading.Semaphore(limit)
empty = threading.BoundedSemaphore(limit)
for i in range(10):
    empty.acquire()

server = rpyc.ThreadedServer(BufferService, port=12345)
print("BufferService ON")
server.start()