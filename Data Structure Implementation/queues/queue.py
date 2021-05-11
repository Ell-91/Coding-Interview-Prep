class Queue:
  def __init__(self):
    self.queue = []

  #O(1)
  #append/add items to end of the list
  def enqueue(self, data):
    self.queue.append(data)
  
  #O(N)  b/c you have to shift when popping from the front
  def dequeue(self):
    if self.size() != 0:
      data = self.queue[0]
      del self.queue[0]
      return self.queue[0]
    else:
      return data
  #O(1)
  def peek(self):
    return self.queue[0]

  #O(1)
  def empty(self):
    return self.queue == []
  
  #O(1)
  def size(self):
    return len(self.queue)

q = Queue()
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.dequeue()

print(q.size())
print(q.peek())