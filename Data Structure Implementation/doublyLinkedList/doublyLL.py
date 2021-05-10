class Node:
  def __init__(self,data):
    self.data = data
    self.next = None 
    self.prev = None

class DoublyLL:
  def __init__(self):
    self.numOfnodes = 0
    self.head = None
    self.tail = None

  def insert_end(self,data):
    self.numOfnodes += 1
    new_node = Node(data)

    #check if list is empty
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node
  
  def insert_front(self,data):
    self.numOfnodes += 1
    new_node = Node(data)

    #check if list is empty 
    if self.tail is None:
      self.tail = new_node
      self.head = new_node 
    else:
      new_node.prev = self.head
      self.head.prev = new_node
      self.head = new_node 
  
  def remove_front(self):
    self.numOfnodes -= 1

    current_node = self.head
    if current_node is None:
      return print("The list is empty")
    else:
      self.current_node.next = self.head
      self.head = current_node 
      self.head.prev = None 

  def remove_end(self):
    self.numOfnodes -= 1

    current_node = self.tail
    if self.tail is None:
      return print("The list is empty")
    else:
      self.current_node.prev = self.tail
      self.tail = current_node 
      self.tail.next = None
  
  def traverse_forwards(self):
    current_node = self.head

    while current_node is not None:
      print(current_node.data)
      current_node = current_node.next 

  
  def traverse_backwards(self):
    current_node = self.tail

    while current_node is not None:
      print(current_node.data)
      current_node = current_node.prev
  
  def size(self):
    return print(self.numOfnodes)

doublyll = DoublyLL()
#doublyll.insert_front(1)
doublyll.insert_front(5)
doublyll.insert_front(2)
doublyll.insert_end("A")
doublyll.insert_end("Z")

#doublyll.traverse_forwards() #[2 1 A Z]   
doublyll.traverse_backwards() 
doublyll.size()

