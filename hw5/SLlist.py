from SLnode import SLnode

# Two special values for boundary nodes
PLUS_INF = 99999
MINUS_INF = -99999

# List class definition used in the skip list
class SLlist:
    def __init__(self):
        self.leftDummy=SLnode(MINUS_INF,"")
        self.rightDummy=SLnode(PLUS_INF,"")
        self.leftDummy.setNext(self.rightDummy)
        self.rightDummy.setPrev(self.leftDummy)
        self.size = 0
        self.insert_cursor = self.getleftDummy()

    def getleftDummy(self):
        return self.leftDummy

    def getrightDummy(self):
        return self.rightDummy

    def getSize(self):
        return self.size

    def increaseSize(self):
        self.size=self.size + 1

    def decreaseSize(self):
        self.size=self.size - 1

    def insertAfter(self, p, SLnode):
        SLnode.setNext(p.getNext())
        SLnode.setPrev(p)
        p.getNext().setPrev(SLnode)
        p.setNext(SLnode)
        self.increaseSize()

    def print_List(self):
        current = self.leftDummy
        while (current != None):
            print("(",current.getKey(),",",current.getItem(),")",sep='',end="")
            current = current.getNext()
        print("")

    def findPosition(self, node):
        while True:
            if self.insert_cursor.key > node.key:
                temp = self.insert_cursor
                self.insert_cursor = self.leftDummy
                print("node in findPosition", temp.prev.key, temp.prev.item)
                return temp.prev
            else:
                print("iterate ", self.insert_cursor.key, self.insert_cursor.item)
                self.insert_cursor = self.insert_cursor.next
