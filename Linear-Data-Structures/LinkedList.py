from Node import Node

class LinkedList:
  """
  A linked list class used to store a list of information
  """

  def __init__(self, value: any = None) -> None:
    """
    Initialises linked list.
    
    Args:
      value: The value of the first node in the list (default: None)
    """

    self.__head = Node(value)
    
  def __str__(self) -> str:
    """
    Gets String format of the linked list.
    
    Returns:
      String of the all the values in the list.
    """

    stringList = ""
    currentNode = self.GetHeadNode()
    while currentNode:
      if currentNode.GetValue() != None:
        stringList += str(currentNode.GetValue()) + "\n"
      currentNode = currentNode.GetNextNode()
    return stringList
  
  def GetHeadNode(self) -> Node:
    """
    Gets the head node.
    
    Returns:
      The head node.
    """

    return self.__head
  
  def Add(self, newValue: any) -> None:
    """
    Adds a new value to the head of the list.
    
    Args:
      newValue: The value of the new node.
    """

    newNode = Node(newValue)
    newNode.SetNextNode(self.__head)
    self.__head = newNode
  
  def Remove(self, valueToRemove: any) -> None:
    """
    Removes a given value from the list.
    
    Args:
      The value to find and remove.
    """

    if (self.__head.GetValue() == valueToRemove):
      self.__head = self.__head.GetNextNode()
    else:
      currentNode = self.__head
      while (currentNode != None):
        if (currentNode.GetNextNode().GetValue() == valueToRemove):
          currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
          currentNode = None
        else:
          currentNode = currentNode.GetNextNode()
