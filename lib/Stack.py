class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) >= self.limit:
            return True
        else:
            return False

    def search(self, target):
        # if target in self.items:
        index = self.items.index(target)
        dist_top = len(self.items) - (index +1)
        return dist_top
