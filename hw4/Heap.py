from Hnode import Hnode

# Heap class
class Heap:
    def __init__(self):
        self.root=None
        self.last=None
        self.size=0
        self.leafs = []

    def isEmpty(self):
        return (self.size==0)

    def getSize(self):
        return self.size

    def getRoot(self):
        return self.root

    def getLast(self):
        return self.last

    def getHighestPriority(self):
        return self.root.getKey()

    def setRoot(self, hnode):
        self.root=hnode

    def setLast(self, hnode):
        self.last=hnode

    def findLeafs(self, i):

        if not i:
            return
        if i.isLeaf():
            i.depth = i.Depth()
            self.leafs.append(i)
        if i.hasLeftChild():
            self.findLeafs(i.getLeftChild())
            if i.hasRightChild():
                self.findLeafs(i.getRightChild())
        return self.leafs

    def findLast(self):
        leafs = self.findLeafs(self.root)
        depth = 0
        node = None
        for leaf in leafs:
            if leaf.depth > depth or (leaf.depth == depth and leaf.isRightChild()):
                depth = leaf.depth
                node = leaf
        return node

    def findNewLast(self):
        leafs = self.findLeafs(self.root)
        depth = leafs[0].depth
        node = leafs[0]

        for leaf in leafs:
            if leaf.depth != depth:
                node = leaf
                return node

        return node


    #
    # For management, print the heap in pre-order
    #
    def printHeapPreOrder(self, i):
        if not i:
            return
        if i.isLeaf():
            print("Leaf [", i.getKey(), i.getItem(), "]")
        elif i.isRoot():
            print("Root [", i.getKey(), i.getItem(), "]")
        else:
            print("Node [", i.getKey(), i.getItem(), "]")
        if i.hasLeftChild():
            self.printHeapPreOrder(i.getLeftChild())
            if i.hasRightChild():
                self.printHeapPreOrder(i.getRightChild())
    #
    # The most important operation for a heap, remove_Min (extract_Min())
    #
    def removeMin(self):
        if self.isEmpty():
            print("The heap is now empty and no entry can be removed")
        else:
            print("Node [", self.root.getKey(), self.root.getItem(), " ]")
            self.root.change(self.last)
            if self.last.isRightChild():
                self.last.getParent().right = None
                self.last = self.findLast()
            if self.last.isLeftChild():
                self.last.getParent().left = None
                self.last = self.findLast()

            self.downwardHeapify(self.root)
            self.size = self.size - 1
            if self.size == 0:
                print("The heap is now empty")

    #
    # downward adjustment from current node
    #
    def downwardHeapify(self,current):
        current.changeDown()

    #
    # upward adjustment toward the root from the current node
    #
    def upwardHeapify(self, current):
        current.changeParent()

    #
    # Another important operation for a heap, insertion() (add())
    #
    def Insert(self, hnode):
        if self.isEmpty():
            self.setRoot(hnode)
            self.last = self.root

        elif self.root == self.last:
            self.last.addLeftChild(hnode)
            self.last = self.last.getLeftChild()
            self.last.changeParent()


        elif self.last.isLeftChild():
            self.last.parent.addRightChild(hnode)
            self.last = self.last.parent.right
            self.last.changeParent()

        elif self.last.isRightChild():
            self.last = self.findNewLast()
            self.last.addLeftChild(hnode)
            self.last = self.last.left
            self.last.changeParent()

        self.size = self.size + 1

