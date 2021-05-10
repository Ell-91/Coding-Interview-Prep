#class for Node 
class Node:
  def __init__(self, data):
    self.data = data #every node stores the data
    self.next = None #every node references the next node

#class for the LL
class linkedList:
  def __init__(self):
    self.head = None #reference first node of the LL, its NULL b/c it is empty at the beginning
    self.numOfnodes = 0 #reference to the number of nodes, it's empty in the beginning
  
  def insert_start(self, data): #--> O(1)
    self.numOfnodes += 1
    new_node = Node(data) #instantiate a new node

    #check if it is the first node of the LL// check if head node is None
    #If head node is None it means the LL is empty
    #   and we have to initialize the head node
    if not self.head: #if self.head is not NONE LL is empty (if this is true)
      self.head = new_node
    else: #we know the LL is not empty
      new_node.next = self.head #whatever was the head previously
      self.head = new_node

  def insert_end(self, data):  #--> O(N)
    self.numOfnodes += 1
    new_node = Node(data) #instantiate a new node

    current_node = self.head
    while current_node.next is not None:
      current_node = current_node.next #hope from node to node to find the last node in the structure 

    #Once node is None we have reached the end of the list
    current_node.next = new_node

  def remove(self, data):
    self.numOfnodes -= 1
    if self.head is None: #LL is empty, doesn't return anything
      return print("The Linked list is empty")
    
    current_node = self.head
    prev_node = None 

    #delete arbitrary node search for node and update references
    while current_node is not None and current_node.data != data:
      prev_node = current_node
      current_node = current_node.next
    
    #if the current_node is None
    if current_node is None:
      print("The node is not present in the list")

    if prev_node is None:
      self.head = current_node.next
    else:
      prev_node.next = current_node.next
    

  def sizeLinkedList(self): #-->O(N)
    return self.numOfnodes

  def traverse(self): #---> O(N)
    #store a reference to the actual node
    current_node = self.head 

    while current_node is not None: #we are not at the end of the linkedlist
      print(current_node.data)
      current_node = current_node.next


llist = linkedList()
llist.insert_start("A")
llist.insert_start("B")
llist.insert_start("C")
llist.insert_end("5")

llist.remove("17")
llist.traverse()
print(llist.sizeLinkedList())





      

    