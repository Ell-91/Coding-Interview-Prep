class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class linkedList:
  def __init__(self):
    self.head = None
    self.numOfNodes = 0

  def prepend(self,data):
    self.numOfNodes += 1
    new_node = Node(data)
    
    #Dont need to check if list is NULL b/c if it is we'll just prepend
    new_node.next = self.head
    self.head = new_node
  
  def append(self,data):
    self.numOfNodes += 1
    new_node = Node(data)

    if self.head is None: #list is empty
      self.head = new_node
      return
    
    current_node = self.head 

    while current_node is not None:
      current_node = current_node.next
    current_node.next = new_node

  #Assume no duplicated
  #traverse the list to find the node to be deleted 
  # Two cases
  #  1. Node is the head (edge case)
  #  2. Node is not the head
  def delete(self,key):
    self.numOfNodes -= 1
    current_node = self.head

    #Delete head node
    if current_node is not None and current_node.data == key: #if current node is not None and is equal to the data we seek, do these steps
      self.head = current_node.next #set the head to be the next node in the list
      current_node = None
      return

    #Delete a node that is note the head
    prev_node = None

    while current_node is not None and current_node.data != key:   #while current_node not None == while current_node
      prev_node = current_node
      current_node = current_node.next
    
    #if head is NULL return
    if current_node is None:
      return print("The element in the list is not present")
    
    #otherwise the element it is present 
    #prev_node.next points to the one to be deleted
    prev_node.next = current_node.next
    current_node = None




  def print(self):
    current_node = self.head

    while current_node:  #or while current_node is not None
      print(current_node.data)
      current_node = current_node.next
  
  def size(self):
    return self.numOfNodes

llist = linkedList()
llist.prepend("A")
llist.prepend("B")
llist.prepend("C")
llist.print()
print(llist.size())





 

    current_node = self.head

    #Delete head node
    if current_node is not None and current_node.data == key: #if current node is not None and is equal to the data we seek, do these steps
      self.head = current_node.next #set the head to be the next node in the list
      current_node = None
      return

    #Delete a node that is note the head
    prev_node = None

    while current_node is not None and current_node.data != key:   #while current_node not None == while current_node
      prev_node = current_node
      current_node = current_node.next
    
    if current_node is None:
      return print("The element in the list is not present")
    
    prev_node.next = current_node.next
    current_node = None
