#class for the node object
class Node:
  def __init__(self,data): #constructor, every node consists of self and data
    self.data = data
    self.next = None

#inter that points to the he
#class for the actual linkedlist itself  
class linkedList:
  def __init__(self): 
    self.head = None  #head poad of the list
    self.numOfNodes = 0
  
  def print_list(self):
    current_node = self.head
    while current_node:  #while current node doesnt equal NULL 
      print(current_node.data)
      current_node = current_node.next

  #need to traverse the list to get to the end 
  def append(self, data):
    self.numOfNodes += 1
    new_node = Node(data) #Use our node class to define a new_node and set it equal to the node object and pass it data

    #check if the list is empyty, if so append to it
    if self.head is None:  
      self.head = new_node
      return
    #if list is not empty and there are other entries in the list
    last_node = self.head #last node is equal to the start of the list

    while last_node.next: #while the next pointer of the node we are currently on isn't NULL we continue on in this loop 
      last_node = last_node.next #move head pointer to the right 
   
    last_node.next = new_node  #when loop has concluded last_node will point to the last node


  def prepend(self, data):
    self.numOfNodes += 1
    new_node = Node(data)

    #make it point to the current head of the list
    new_node.next = self.head #We have the new node we created and we want the next field of the node to point to point to the head of the list
    self.head = new_node

  #insert after a given node in the list 
  def insert_arbitrarily(self, prev_node, data):
    
    #determine if the previous node is present in the list
    if not prev_node:   #if prev_node is not in the list
      print("Previous node is not in the list")
      return

    new_node = Node(data)

    new_node.next = prev_node.next   #At this point two pointers are pointing to the same element
    prev_node.next = new_node




#LL Delete a node given a data field (assume no duplictes)
#Two cases
  # 1. Node to be deleted is head
  # 2. Node to be deleted is not head
  def delete(self,data_key):
    current_node = self.head #set curret node to be the head of the list
    
    #Case 1: delete the head node
    #first check if the head node is the node to be deleted
    if current_node and current_node.data == data_key:  #if current_node is not None (list is not empty)  and the data is equal to the key, then go through steps
      
    #setting the head equal to the next node in the list
      self.head = current_node.next
      current_node = None   #delete the previous node 

    #Case 2: delete a node that is not the head of the list
    #Find the nodes before and after the node we want to delete
    #current_node = self.head
    prev_node = None
    while current_node and current_node.data != data_key:  #while the head node is not None and while the data fields of the nodes we encounter aren't equal to the key
      prev_node = current_node #current_node = self.head
      current_node = current_node.next  #moves the head point along
    
    #if current_node = NULL then the element isn't in the list
    if current_node is None: #The element in the list is not present
      return 

    prev_node.next = current_node.next
    current_node = None

  def delete_position(self, position, data):

llist = linkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")


#print(llist.head.data) #---> A
#print(llist.head.next.data) #---> B

#llist.insert_arbitrarily(llist.head.next, "E")
#llist.print_list()

llist.delete("B")
llist.print_list()
