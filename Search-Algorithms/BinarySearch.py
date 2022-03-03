class BinarySearch:
    """
    Class to perform binary searches to find index of given value in a given list.
    """

    def __init__(self) -> None:
        """
        Initialises BinarySearch class.
        """

        pass

    def findIndexOfValue(self, searchList: list, target: any, pLeft: int, pRight: int) -> int:
        """
        Find index of a given value via recursion.
        
        Args:
            searchList: The list to be searched.
            target: The value to be found.
            pLeft: Index of the left most value in list.
            pRight: Index of the right most value in list.
        
        Returns:
            Index of target value.
            
        Raises:
            ValueError: If `target` is not in `searchList`.
        """

        if pLeft >= pRight:
            raise ValueError("{0} not in list".format(target))
        midIdx = (pLeft + pRight) // 2
        midVal = searchList[midIdx]
        if midVal == target:
            return midIdx
        elif midVal > target:
            return self.findIndexOfValue(searchList, target, pLeft, midIdx)
        elif midVal < target:
            return self.findIndexOfValue(searchList, target, midIdx + 1, pRight)