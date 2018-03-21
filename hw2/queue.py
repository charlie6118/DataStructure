class Queue:
    def __init__(self):
        self.item = []
    def isEmpty(self):
        return self.item == []
    def enqueue(self, item):
        self.item.insert(0, item)
    def size(self):
        return len(self.item)
    def dequeue(self):
        return self.item.pop()
    def show(self, index):
        print(self.item[index])