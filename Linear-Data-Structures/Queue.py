from Node import Node


class Queue:
    def __init__(self, value: any = None, maxSize: int = None) -> None:
        """
        Initialises queue class.
        
        Args:
            value: Value of the first item in the queue (default: None).
            maxSize: The maximum size of the queue (default: None).
        """

        self.__maxSize = maxSize
        self.__size = 1
        newNode = Node(value)
        self.__head = newNode
        self.__tail = newNode

    def __str__(self) -> str:
        """
        Returns a string representation of the queue.
        
        Returns:
            String representation of the queue.
        """

        stringQueue = ""
        currentNode = self.__head()
        while currentNode:
            if currentNode.GetValue() != None:
                stringQueue += str(currentNode.GetValue()) + "\n"
            currentNode = currentNode.GetNextNode()
        return stringQueue

    def GetSize(self) -> int:
        """
        Gets the current size of the queue.
        
        Returns:
            Current size of the queue.
        """

        return self.__size

    def HasSpace(self) -> bool:
        """
        Checks if the queue has space.
        
        Returns:
            True if the queue has space.
        """

        if self.__maxSize == None:
            return True
        else:
            return self.__size < self.__maxSize

    def IsEmpty(self) -> bool:
        """
        Checks if the queue is empty.
        
        Returns:
            True if the queue is empty.
        """

        return self.__size == 0

    def Peek(self) -> any:
        """
        Reveals data from the front of the queue without removing it.

        Returns:
            The first value in the queue.

        Raises:
            ValueError: if queue is empty.
        """

        if self.__size > 0:
            return self.__head.GetValue()
        else:
            raise ValueError("The Queue is empty")

    def Enqueue(self, value: any) -> None:
        """
        Adds a value to the end of the queue.
        
        Args:
            value: The value to be added to the queue.

        Raises:
            ValueError: If there is no more space in queue.
        """

        if self.HasSpace():
            newNode = Node(value)
            if self.IsEmpty():
                self.__head = newNode
                self.__tail = newNode
            else:
                self.__tail.SetNextNode(newNode)
                self.__tail = newNode
            self.__size += 1
        else:
            raise ValueError("No more space in queue")

    def Dequeue(self) -> any:
        """
        Removes the first value from the queue and returns its value.
        
        Returns:
            The first value in the queue.
            
        Raises:
            Value Error: If the queue is empty.
        """

        if self.GetSize() > 0:
            removeNode = self.__head
            if self.GetSize() == 1:
                self.__head = None
                self.__tail = None
            else:
                self.head = removeNode.GetNextNode()
            self.__size -= 1
            return removeNode.GetValue()
        else:
            raise ValueError("The Queue is empty")