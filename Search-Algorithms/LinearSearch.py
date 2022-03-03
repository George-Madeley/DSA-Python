class LinearSearch:
    """
    Class to perform linear searches to find indexes, maximum, and minimum value in a given list.
    """

    def __init__(self) -> None:
        """
        Initialises LinearSearch class.
        """

        pass

    def FindIndexOfValue(self, searchList: list, target: any) -> int:
        """
        Finds the first index of a given value.
        
        Args:
            searchList: The list to be searched.
            target: The value to be found.

        Returns:
            The index of the value if found.

        Raises:
            ValueError: If `target` is not in `searchList`.
        """

        for index in range(len(searchList)):
            if searchList[index] == target:
                return index
        raise ValueError("{0} not in list".format(target))

    def FindIndexesOfValue(self, searchList: list, target: any) -> list[int]:
        """
        Finds all indexes of a given value.

        Args:
            searchList: The list to search.
            target: The value to be found.

        Returns:
            A list of all found indexes.

        Raises:
            ValueError: if `target` is not in `searchList`.
        """

        indexes = []
        for index in range(len(searchList)):
            if searchList[index] == target:
                indexes.append(index)
        if len(indexes) != 0:
            return indexes
        raise ValueError("{0} not in list".format(target))

    def FindMaximum(self, searchList: list) -> any:
        """
        Finds and returns the maximum value in the list.
        
        Args:
            searchList: The list to be searched.
            
        Returns:
            The maximum value in the list.
        """

        maximum = None
        for index in range(len(searchList)):
            if maximum == None or searchList[index] > maximum:
                maximum = searchList[index]
        return maximum

    def FindMinimum(self, searchList: list) -> any:
        """
        Finds the minimum value in the list.
        
        Args:
            searchList: The list to be searched.
            
        Returns:
            The minimum value in the list.
        """

        minimum = None
        for index in range(len(searchList)):
            if minimum == None or searchList[index] < minimum:
                minimum = searchList[index]
        return minimum