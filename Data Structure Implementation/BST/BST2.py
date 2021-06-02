class Node:
  def __init__(self,data): #our constructor takes self and node
    self.data = data #set the class variable(self.data) to whatever is passed into the constructor
    self.left_node = None #everynode has a left and right child
    self.right_node = None

class BinarySearchTree:
  def __init__(self): #for the constructor of this class we just set the root variable to None
    self.root = None

  def insert(self,data): #going to take self, the member of the class and data
    if self.root is None:
      self.root = Node(data) #construct a node and set the root of the tree to this node
    else:
      self.insert_node(data, self.root)

  def insert_node(self,data,current_node):
    if data < current_node.data: #move left
      if current_node.left_node is None:
         current_node.left_node = Node(data, current_node.left_node)
      else:
        self.insert_node(data, current_node.left_node)
     
    elif data > current_node.data:
      if current_node.righ_node is None:
        current_node.right_node = Node(data, current_node.right_node)
      else:
        self.insert_node(data, current_node.left_node)
    else: #element already exists
      print("Value is already present in tree")
  
  def traverse(self):
    if self.root is not None:
      self.traverse_(self.root)

  def traverse_(self,current_node):
    if current_node.left_node:
      self.traverse(current_node.left_node)
    
    print('%s' % current_node.data)

    if current_node.right_node:
      self.traverse(current_node.right_node)

  def get_max(self,node):
    if node.right_node:
      return self._max(node.right)

  def max_(self, node):
    if node.right_node is not None:
      self.max()


bst = BinarySearchTree()
bst.insert(5)
bst.insert(4)