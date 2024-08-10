class QueueError(IndexError):  # Eligir la clase base para la nueva excepción.
    pass

    #
    #  Escribe código aquí.
    #


class Queue:
    def __init__(self):
        self.queue=[]
        #
        # Escribe código aquí.
        #

    def put(self, elem):
        self.queue.append(elem)
        #
        # Escribe código aquí.
        #

    def get(self):
        if len(self.queue)>0:
            elem=self.queue[0]
            del self.queue[0]
            return elem
        else:
            raise QueueError
        #
        # Escribe código aquí.
        #


que = Queue()
que.put(1)
que.put("perro")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Error de Cola")
