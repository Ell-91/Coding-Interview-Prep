class Stack:
  def __init__(self):
    self.stack = []

  def push(self, data):
    self.stack.append(data)

  def pop(self):
    data = self.stack[-1] #find the last element we inserted 
    del self.stack[-1] #remove the given item
    return data

  def peek(self):
    return self.stack[-1]

  def empty(self):
    return self.stack == []
    
  def size(self):
    return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.pop())   #should pop 4
print(stack.peek()) #should return [3, 2, 1]