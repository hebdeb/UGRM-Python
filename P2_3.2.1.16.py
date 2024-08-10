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

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    def isempty(self):
        return len(self.queue)==0
    #
    # Escribe código nuevo aquí.
    #


que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Cola vacía")
