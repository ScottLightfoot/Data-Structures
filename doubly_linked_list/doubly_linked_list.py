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

    def strike_node(self, node_in):
        prvn = node_in.prev
        nxtn = node_in.next
        if node_in is self.head:
            if nxtn == None:
                self.head = None
                self.tail = None
            else:
                self.head = node_in.next
                self.head.prev = None
        elif node_in is self.tail:
            self.tail = node_in.prev
            self.tail.next = None
        else:
            prvn.next = nxtn
            nxtn.prev = prvn
        return node_in
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.length += 1
        if self.length == 1:
            first_node = ListNode(value, None, None)
            self.head = first_node
            self.tail = first_node
        else:
            curr_head = self.head

            new_head = ListNode(value, None, curr_head)
            curr_head.prev = new_head
            self.head = new_head
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length > 0:
            self.length -= 1
            return self.strike_node(self.head).value

        # head_val = self.head.value
        # new_head = self.head.next
        # self.head = new_head
        # self.head.prev = None
        # return head_val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.length += 1
        if self.length == 1:
            first_node = ListNode(value, None, None)
            self.head = first_node
            self.tail = first_node
        else:
            curr_tail = self.tail

            new_tail = ListNode(value, curr_tail, None)
            curr_tail.next = new_tail
            self.tail = new_tail

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length > 0:
            self.length -= 1
            return self.strike_node(self.tail).value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        self.strike_node(node)
        self.length -= 1
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        self.strike_node(node)
        self.length -= 1
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1
        self.strike_node(node)

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
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