class Node:
    """
    A node class to be used in all data structures.
    """

    def __init__(self, value: any, nextNode=None, prevNode=None) -> None:
        """
        Initialises the node class.

        Args:
            value: The nodes value.
            nextNode: A pointer to the next node (default: None).
            prevNode: A pointer to the previous node (default: None).
        """

        self.__value = value
        self.__nextNode = nextNode
        self.__prevNode = prevNode

    def GetValue(self) -> any:
        """
        Gets the nodes value.
        
        Returns:
            The nodes value.
        """

        return self.__value

    def GetNextNode(self) -> 'Node':
        """
        Gets the next node.
        
        Returns:
            The next node.
        """

        return self.__nextNode
    
    def SetNextNode(self, nextNode: 'Node') -> None:
        """
        Sets the next node.
        
        Args:
            nextNode: the new next node.
        """

        self.__nextNode = nextNode

    def GetPrevNode(self) -> 'Node':
        """
        Gets the previous node.
        
        Returns:
            The previous Node.
        """

        return self.__prevNode

    def SetPrevNode(self, prevNode: 'Node') -> None:
        """
        Sets the previous node.
        
        Args:
            prevNode: the new previous node.
        """

        self.__prevNode = prevNode