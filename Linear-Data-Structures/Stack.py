from Node import Node

class Stack:
    """
    A data structure to store information in a stack.
    """

    def __init__(self, value: any, maxSize: int = None) -> None:
        """
        Initializes the Stack.
        
        Args:
            value: The value of the first item in the stack.
            maxSize: The maximum size the stack can be.
        """

        newNode = Node(value)
        self.__head = newNode
        self.__size = 1
        self.__maxSize = maxSize

    def __str__(self) -> str:
        """
        Returns a string representation of the stack.
        
        Returns:
            String representation of the stack.
        """
            
        stringStack = ""
        currentNode = self.__head
        while currentNode:
            if currentNode.GetValue() != None:
                stringStack += str(currentNode.GetValue()) + "\n"
            currentNode = currentNode.GetNextNode()
        return stringStack

    def HasSpace(self) -> bool:
        """
        Checks if the stack has space.
        
        Returns:
            True if there is space within the stack.
        """

        if self.__maxSize == None:
            return True
        else:
            return self.__size < self.__maxSize

    def IsEmpty(self) -> bool:
        """
        Checks if the stack is empty.
        
        Returns:
            True if the stack is empty.
        """

        return self.__size == 0

    def Peek(self) -> any:
        """
        Returns data from the top of the stack without removing it.
        
        Returns:
            The data from the top of the stack.
        
        Raises:
            ValueError: If the stack is empty.
        """

        if not self.IsEmpty():
            return self.__head.GetValue()
        else:
            raise ValueError("Cannot peek a value from an empty stack.")

    def Pop(self) -> any:
        """
        Returns and removes data from the top of the stack.
        
        Returns:
            The data from the top of the stack.
            
        Raises:
            ValueError: If the stack is empty.
        """

        if not self.IsEmpty():
            removeNode = self.__head
            self.__head = removeNode.GetNextNode()
            self.__size -= 1
            return removeNode.GetValue()
        else:
            raise ValueError("Cannot pop a value from an empty stack")

    def Push(self, value: any) -> None:
        """
        Adds a new value to the top of the stack.
        
        Args:
            value: The new value to add.
            
        Raises:
            ValueError: If the stack is full.
        """

        if self.HasSpace():
            newNode = Node(value)
            newNode.SetNextNode(self.__head)
            self.__head = newNode
            self.__size += 1
        else:
            raise ValueError("Cannot push a value on to a full stack")