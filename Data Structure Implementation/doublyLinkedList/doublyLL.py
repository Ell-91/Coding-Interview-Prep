class Node:
  def __init__(self,data):
    self.data = data
    self.next = None 
    self.prev = None

class DoublyLL:
  def __init__(self,data):
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
  
  def inset_front(self,data):
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

  def remove_end(self):
    self.numOfnodes -= 1
  
  def traverse_forwards(self):
  
  def traverse_backwards(self):
  
  def size(self):
    


