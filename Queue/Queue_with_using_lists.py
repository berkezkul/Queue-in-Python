class Queue():
    def __init__(self):
        self.elements= []

    def isEmpty(self):
        return self.elements == []

    def enqueue(self, element):                 #if we use append, this will be stack. With insert, we add to the beginning
        self.elements.insert(0, element)

    def dequeue(self):
        self.elements.pop()

    def size(self):
        return len(self.elements)

    def display(self):
        if (self.isEmpty()):
            print("stack is empty")
        else:
            for item in self.elements:
                print(item)


myQueue = Queue()
myQueue.enqueue(9)                           #9
myQueue.enqueue(3)                           #3, 9
myQueue.enqueue(54)                          #54, 3, 9
myQueue.enqueue(17)                          #17, 54, 3, 9
myQueue.display()

myQueue.dequeue()                            #17, 54, 3        #FIFO (9 by bye)
myQueue.display()

