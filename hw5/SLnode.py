
# Node class definition: a quadraic node having four links
class SLnode:
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.up = None
        self.down = None
        self.next = None
        self.prev = None

    def getKey(self):
        return self.key

    def getItem(self):
        return self.item

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev

    def getUp(self):
        return self.up

    def getDown(self):
        return self.down

    def hasNext(self):
        return (self.next!=None)

    def hasPrev(self):
        return (self.prev!=None)

    def setKey(self, key):
        self.key = key

    def setItem(self, item):
        self.item = item

    def setNext(self, p):
        self.next = p

    def setPrev(self, p):
        self.prev =p

    def setUp(self, p):
        self.up = p

    def setDown(self, p):
        self.down = p


