from Node import Node

class DoubleLinkedList:
  """
  A double linked list to store data.
  
  Allows you to traverse through the
  list forwards and backwards."""
  def __init__(self) -> None:
    """
    Initialises the double linked list.
    """

    self.__head = None
    self.__tail = None

  def __str__(self) -> str:
    """
    Gets the string format of the double linked list.
    
    Returns:
      String format of the double linked list.
    """

    stringList = ""
    currentNode = self.__head
    while currentNode != None:
      if currentNode.GetValue() != None:
        stringList += str(currentNode.GetValue()) + "\n"
      currentNode = currentNode.GetNextNode()
    return stringList

  def AddHead(self, newValue: any) -> None:
    """
    Adds a value to the head end of the list.
    
    Args:
      newValue: The new value to be added.
    """

    newNode = Node(newValue)
    oldHead = self.__head
    if oldHead != None:
      newNode.SetNextNode(oldHead)
      oldHead.SetPrevNode(newNode)
    self.__head = newNode
    if self.__tail == None:
      self.__tail = newNode

  def AddTail(self, newValue: any) -> None:
    """
    Adds a value to the tail end of the list.
    
    Args:
      newValue: The new value to be added.
    """

    newNode = Node(newValue)
    oldTail = self.__tail
    if oldTail != None:
      newNode.SetPrevNode(oldTail)
      oldTail.SetNextNode(newNode)
    self.__tail = newNode
    if self.__head == None:
      self.__head = newNode

  def RemoveHead(self) -> any:
    """
    Removes the first value in the list.

    Returns:
      The first value
    """

    removeHead = self.__head
    if removeHead == None:
      return None
    nextNode = removeHead.GetNextNode()
    if nextNode != None:
      nextNode.SetPrevNode(None)
    self.__head = nextNode
    if self.__tail == removeHead:
      self.RemoveTail()
    return removeHead.GetValue()

  def RemoveTail(self) -> any:
    """
    Removes the last value in the list.
    
    Returns:
      The last value.
    """

    removeTail = self.__tail
    if removeTail == None:
      return None
    prevNode = removeTail.GetPrevNode()
    if prevNode != None:
      prevNode.SetNextNode(None)
    self.__tail = prevNode
    if self.__head == removeTail:
      self.RemoveHead()
    return removeTail.GetValue()

  def RemoveByValue(self, valueToRemove: any) -> Node:
    """
    Removes the given value from the list.
    
    Args:
      valueToRemove: The value to be removed from list.

    Returns:
      The node to be removed.
    """
    currentNode = self.__head
    nodeToRemove = None
    while currentNode != None:
      if currentNode.GetValue() == valueToRemove:
        nodeToRemove = currentNode
        break;
      currentNode = currentNode.GetNextNode()

    if nodeToRemove == None:
      return None

    if nodeToRemove == self.__head:
      self.RemoveHead()
    elif nodeToRemove == self.__tail:
      self.RemoveTail()
    else:
      prevNode = nodeToRemove.GetPrevNode()
      nextNode = nodeToRemove.GetNextNode()
      prevNode.SetNextNode(nextNode)
      nextNode.SetPrevNode(prevNode)
    return nodeToRemove

  