"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.vals = []
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.vals.insert(0, value)
        self.size += 1

    def dequeue(self):
        if len(self.vals) > 0:
            self.size -= 1
            return self.vals.pop()

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         if len(self.storage) > 0:
#             self.size -= 1
#             self.storage.reverse()
#             que_val = self.storage.pop()
#             self.storage.reverse()
#             return que_val
