class Node:
  def __init__(self,data):
    self.data = data
    self.leftNode = None
    self.rightNode = None

class BinarySearchTree:
  def __init__(self):
    self.root = None
  
  def insert(self,data):
    if self.root is None:
      self.root = Node(data)
    else:
      self.insert_node(data, self.root)
  
  def insert_node(self,data,cur_node):
    if data < cur_node.data:
      if cur_node.leftNode:
        self.insert_node(data,cur_node.leftNode)
      else:
        cur_node.leftNode = Node(data)
    else :
      if cur_node.rightNode:
        self.insert_node(data,cur_node.rightNode)
      else:
        cur_node.rightNode = Node(data)

def traverse(self):
  if self.root is not None:
    return self.traverse_in_order(self.root)

def traverse_in_order(self, node):
  if node.leftNode:
    return traverse(node.leftChild)

  print('%s' % node.data)

  if node.rightChild:
    return traverse(node.rightChild)

#check if BST is empty,if not call rightNode until
#  you get to last node and that node is the MAX
def get_max_value(self):
  if self.root:
    return self.getMax(self.root)

def getMax(self,node):
  if node.rightNode:
    return get_max_value(node.rightNode)

  #keep considering the rightmost child 
  # until the node is None, then we know 
  # that  the node is the rightmost item and we
  # return with the nodes data (node.data) 
  return node.data

def get_min_value(self):
  if self.root:
    return self.getMin(self.root)

def getMin(self,node):
  if node.leftNode:
    return get_min_value(node.leftNode)

def find(self,data): #want to find a node that has the data element
  if self.root:
    is_found = self.find_value(data,self.root) #returns a boolean value to let us knw if the value is in the tree
    if is_found:
      return True
    return False 

  else:
    return None #no nodes in the tree

def find_value(self,data, node):
  if data > node.data and node.rightNode: #and right node exists
    return self.find_value(data, node.rightNode)
  elif data < node.data:
    return self.find_value(data,node)
  
  #returns true if we find data element
  if data == node.data:
    return True
