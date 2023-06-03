# Queue-in-Python

I covered the implementation of the Queue data structure.
  First of all, with the __init__ method I created, I created a list (items) to store the head, end (tail) and elements of the queue. I took the size parameter to specify the list size.

I checked if the queue is empty with the is_empty method. I did this by checking if the head and tail indices were equal.

The is_full method, I checked if the queue is full. Using the (tail + 1) % len(items) expression, I moved the tail index to the next position and then checked if it was equal to the head index. Getting the mod will return the remainder of the self.tail divided by len(self.items). This will cause the value to return to the beginning of the list when the self.tail value rises above the size of the list (len(self.items)), so I used a modal take.

  I calculated the number of elements in the queue with the count method. Using the expression (tail - head + len(items)) % len(items) I have calculated a circular queue.

With the size method, I returned the total size of the queue.

I added a new element to the queue with the enqueue method. First, I checked if the queue is full with the is_full method. If it's full, I've printed an error message. If it's not full, I've moved the tail index to the next position by assigning the new element to the tail index.

I removed an element from the queue with the dequeue method. First, I checked if the queue is empty with the is_empty method. If it's blank, I've printed an error message. If it's not empty, I moved the head index to the next position by removing the element in the head index.

I printed the elements in the queue to the screen with the display method. First, I checked if the queue is empty with the is_empty method. If it's blank, I've printed an error message. I finished my code by printing the elements from head index to tail index if it is not empty.
