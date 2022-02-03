class LinearSearch:
    def __init__(self):
        pass

    def findIndexOfValue(self, list, value):
        for index in range(len(list)):
            if list[index] == value:
                return index
        raise ValueError("{0} not in list".format(value))

    def findIndexesOfValue(self, list, value):
        indexes = []
        for index in range(len(list)):
            if list[index] == value:
                indexes.append(index)
        if len(indexes) != 0:
            return indexes
        raise ValueError("{0} not in list".format(value))

    def findMaximum(self, list, value):
        maximum = None
        for index in range(len(list)):
            if maximum == None or list[index] > maximum:
                maximum = list[index]
        return maximum

    def findMinimum(self, list, value):
        minimum = None
        for index in range(len(list)):
            if minimum == None or list[index] < minimum:
                minimum = list[index]
        return minimum