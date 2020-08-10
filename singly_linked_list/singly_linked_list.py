class Node:
    def __init__(self, val_in, next_node=None):
        self.value = val_in
        self.next_node = next_node

    def get_val(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def remove_head(self):
        if self.head is not None:
            val_out = self.head.get_val()
            self.head = self.head.get_next()
            if self.head == None:
                self.tail = None
            return val_out
        else:
            return None
    
    def contains(self, val):
        if self.head is not None:
            curr = self.head
            while curr.get_next() is not None:
                if curr.get_val() == val:
                    return True
                else:
                    curr = curr.get_next()
            if curr.get_val() == val:
                return True
            return False
        else:
            return None
    
    def get_max(self):
        if self.head == None:
            return None
        else:
            max_val = 0
            curr = self.head
            while curr.get_next() is not None:
                max_val = max(max_val, curr.get_val())
                curr = curr.get_next()
        return max(max_val, curr.get_val())

