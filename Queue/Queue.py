class Queue():
    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.items = [None] * size

    def is_empty(self):
        return self.head == self.tail
    
    def is_full(self):
        return (self.tail + 1) % len(self.items) == self.head

    def count(self):
        return (self.tail - self.head + len(self.items)) % len(self.items)

    def size(self):
        return len(self.items)

    def enqueue(self, element):
        if self.is_full():
            print("Queue is full. Cannot enqueue element!")
        else:
            self.items[self.tail] = element
            self.tail = (self.tail + 1) % self.size()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue element!")
        else:
            dequeued_element = self.items[self.head]
            self.head = (self.head + 1) % self.size()
            return dequeued_element

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            current_index = self.head
            while current_index != self.tail:
                print(self.items[current_index])
                current_index = (current_index + 1) % self.size()


myQueue = Queue(6)

myQueue.enqueue(35)
myQueue.enqueue(6)
myQueue.enqueue(16)
print("My queue is: ")
myQueue.display()
myQueue.dequeue()

myQueue.enqueue(48)
myQueue.enqueue(34)
print("My queue is: ")
myQueue.display()

