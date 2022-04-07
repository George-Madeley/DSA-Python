class MinHeap:
    def __init__(self):
        self.list = [None]
        self.count = 0

    def Add(self, element):
        self.count += 1
        self.list.append(element)

    def ParentIndex(self, index):
        return index // 2
    
    def LeftChildIndex(self, index):
        return index * 2

    def RightChildIndex(self, index):
        return index * 2 + 1

    def HeapifyUp(self):
        index = len(self.list) - 1
        while self.ParentIndex > 0:
            child = self.list[index]
            parent = self.list[self.ParentIndex(index)]
            if parent > child:
                self.list[index] = parent
                self.list[self.ParentIndex(index)] = child
            index = self.ParentIndex(index)

    def HeapifyDown(self):
        index = 1
        while self.LeftChildIndex(index) <= self.count:
            smallerChildIndex = self.GetSmallerChildIndex(index)
            child = self.list[smallerChildIndex]
            parent = self.list[index]
            if parent > child:
                self.list[smallerChildIndex] = parent
                self.list[index] = child
            index = smallerChildIndex

    def RetrieveMin(self):
        if self.count == 0: return None
        min = self.list[1]
        self.list[1] = self.list.pop()
        self.count -= 1
        return min

    def GetSmallerChildIndex(self, index):
        if self.RightChildIndex(index) < self.count:
            return self.LeftChildIndex(index)
        leftChild = self.list[self.LeftChildIndex(index)]
        rightChild = self.list[self.RightChildIndex(index)]
        if leftChild < rightChild:
            return self.LeftChildIndex(index)
        else:
            return self.RightChildIndex(index)

    