class Deque:
    def __init__(self):
        self.item = []
    def isEmpty(self):
        return self.item == []
    def insertFirst(self, item):
        self.item.append(item)
    def insertLast(self, item):
        self.item.insert(0, item)
    def size(self):
        return len(self.item)
    def removeFirst(self):
        return self.item.pop()
    def removeLast(self):
        return self.item.pop(0)