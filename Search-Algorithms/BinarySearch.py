class BinarySearch:
    def __init__(self):
        pass

    def findIndexOfValue(self, searchList, target, pLeft, pRight):
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