class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self, level=0):
        ret = "--->" * level + repr(self.value) + "\n"
        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def addChild(self, childNode):
        self.children.append(childNode)

    def removeChild(self, childNode):
        self.children = [child for child in self.children if child is not childNode]

    