from turtle import left


class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value, self.depth + 1)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value, self.depth + 1)
            else:
                self.left.insert(value)

    def GetNodeByValue(self, value):
        if value == self.value: return self
        elif value < self.value and self.left is not None:
            return self.left.GetNodeByValue(value)
        elif value > self.value and self.right is not None:
            return self.right.GetNodeByValue(value)
        else: return None

    def BreadthFirstTraversal(self):
        frontier = [self]
        while frontier:
            currentNode = frontier.pop(0)
            print(f"Depth = {currentNode.depth}, Value = {currentNode.value}")
            frontier.append(currentNode.left)
            frontier.append(currentNode.right)


    def PreOrderTraversal(self):
        print(f"Depth = {self.depth}, Value = {self.value}")
        if self.left is not None:
            self.left.InOrderTraversal()
        if self.right is not None:
            self.right.InOrderTraversal()

    def InOrderTraversal(self):
        if self.left is not None:
            self.left.InOrderTraversal()
        print(f"Depth = {self.depth}, Value = {self.value}")
        if self.right is not None:
            self.right.InOrderTraversal()

    def PostOrderTraversal(self):
        if self.left is not None:
            self.left.InOrderTraversal()
        if self.right is not None:
            self.right.InOrderTraversal()
        print(f"Depth = {self.depth}, Value = {self.value}")
