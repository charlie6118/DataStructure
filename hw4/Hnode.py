# Node class
class Hnode:
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.parent = None
        self.right = None
        self.left = None
        self.depth = 0

    def getKey(self):
        return self.key

    def getItem(self):
        return self.item

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def getParent(self):
        return self.parent

    def hasRightChild(self):
        return (self.right!=None)

    def hasLeftChild(self):
        return (self.left!=None)

    def isRoot(self):
        return (self.parent==None)

    def isLeaf(self):
        return ((self.right==None)and(self.left==None))

    def isRightChild(self):
        return (self.parent.right==self)

    def isLeftChild(self):
        return (self.parent.left==self)

    def setParent(self, p):
        self.parent=p

    def setKey(self, key):
        self.key = key

    def setItem(self, item):
        self.item = item

    def addRightChild(self, hnode):
        self.right=hnode
        hnode.setParent(self)

    def addLeftChild(self, hnode):
        self.left=hnode
        hnode.setParent(self)

    def changeParent(self):
        if self.key < self.parent.key:
            self.change(self.parent)
            if not self.parent.isRoot():
                self.parent.changeParent()
    def change(self, node):
        tempKey = self.key
        tempItem = self.item
        self.key = node.key
        self.item = node.item
        node.key = tempKey
        node.item = tempItem

    def Depth(self):
        if not self.isRoot():
            self.depth = 1 + self.parent.Depth()
            #self.parent.Depth()
        return self.depth

    def changeDown(self):
        if self.hasRightChild() and self.left.hasLeftChild():
            if (self.right.key > self.left.key) and (self.key > self.right.key):
                self.change(self.left)
                self.left.changeDown()
            if (self.right.key < self.left.key) and (self.key > self.left.key):
                self.change(self.right)
                self.right.changeDown()
            if (self.right.key > self.key) and (self.key > self.left.key):
                self.change(self.left)
                self.left.changeDown()
            if (self.left.key > self.key) and (self.key > self.right.key):
                self.change(self.right)
                self.left.changeDown()

        if self.hasLeftChild() and not self.left.hasRightChild():
            if self.key > self.left.key:
                self.change(self.left)
                self.left.changeDown()
