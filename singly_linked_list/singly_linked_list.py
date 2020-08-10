class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.storage = self.storage.append(value)

    def pop(self):
        return self.storage.pop()