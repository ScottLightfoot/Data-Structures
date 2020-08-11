"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        self.length += 1
        if type(value) is int:
            new_node = ListNode(value, None, None)
        else:
            new_node = value
        
        if self.length == 1:
            self.head = new_node
            self.tail = new_node
        else:
            curr_head = self.head
            new_node.prev = None
            new_node.next = curr_head
            curr_head.prev = new_node
            self.head = new_node

    def add_to_tail(self, value):
        self.length += 1
        if type(value) is int:
            new_node = ListNode(value, None, None)
        else:
            new_node = value

        if self.length == 1:
            self.head = new_node
            self.tail = new_node
        else:
            curr_tail = self.tail
            new_node.prev = curr_tail
            new_node.next = None
            curr_tail.next = new_node
            self.tail = new_node

    def strike_node(self, node_in):
        if node_in is self.head:
            if node_in.next == None:
                self.head = None
                self.tail = None
            else:
                self.head = node_in.next
                self.head.prev = None
        elif node_in is self.tail:
            self.tail = node_in.prev
            self.tail.next = None
        else:
            node_in.prev.next = node_in.next
            node_in.next.prev = node_in.prev
        return node_in

    def delete(self, node):
        self.length -= 1
        self.strike_node(node)

    def remove_from_head(self):
        if self.length > 0:
            self.length -= 1
            return self.strike_node(self.head).value

    def remove_from_tail(self):
        if self.length > 0:
            self.length -= 1
            return self.strike_node(self.tail).value

    def move_to_front(self, node):
        self.length -= 1
        self.add_to_head(self.strike_node(node))

    def move_to_end(self, node):
        self.length -= 1
        self.add_to_tail(self.strike_node(node))

    def get_max(self):
        if self.head == None:
            return None
        else:
            curr = self.head
            max_val = curr.value
            while curr.next is not None:
                max_val = max(max_val, curr.value)
                curr = curr.next
        return max(max_val, curr.value)