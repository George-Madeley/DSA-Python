class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value

class DoubleLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def addHead(self, newValue):
    newNode = Node(newValue)
    oldHead = self.head
    if oldHead != None:
      newNode.set_next_node(oldHead)
      oldHead.set_prev_node(newNode)
    self.head = newNode
    if self.tail == None:
      self.tail = newNode

  def addTail(self, newValue):
    newNode = Node(newValue)
    oldTail = self.tail
    if oldTail != None:
      newNode.set_prev_node(oldTail)
      oldTail.set_next_node(newNode)
    self.tail = newNode
    if self.head == None:
      self.head = newNode

  def removeHead(self):
    removeHead = self.head
    if removeHead == None:
      return None
    nextNode = removeHead.get_next_node()
    if nextNode != None:
      nextNode.set_prev_node(None)
    self.head = nextNode
    if self.tail == removeHead:
      self.removeTail()
    return removeHead.get_value()

  def removeTail(self):
    removeTail = self.tail
    if removeTail == None:
      return None
    prevNode = removeTail.get_prev_node()
    if prevNode != None:
      prevNode.set_next_node(None)
    self.tail = prevNode
    if self.head == removeTail:
      self.removeHead()
    return removeTail.get_value()

  def removeByValue(self, valueToRemove):
    currentNode = self.head
    nodeToRemove = None
    while currentNode != None:
      if currentNode.get_value() == valueToRemove:
        nodeToRemove = currentNode
        break;
      currentNode = currentNode.get_next_node()

    if nodeToRemove == None:
      return None

    if nodeToRemove == self.head:
      self.removeHead()
    elif nodeToRemove == self.tail:
      self.removeTail()
    else:
      prevNode = nodeToRemove.get_prev_node()
      nextNode = nodeToRemove.get_next_node()
      prevNode.set_next_node(nextNode)
      nextNode.set_prev_node(prevNode)
    return nodeToRemove

  def __str__():
    stringList = ""
    currentNode = self.head
    while currentNode != None:
      if currentNode.get_value() != None:
        stringList += str(currentNode.get_value()) + "\n"
      currentNode = currentNode.get_next_node()
    return stringList