"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left == None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left == None:
            pass
        else:
            self.left.for_each(fn)
        if self.right == None:
            pass
        else:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left != None:
            self.left.in_order_print()
        print(self.value)
        if self.right != None:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        queue = []

        queue.append(self)

        while len(queue) > 0:
            next_node = queue.pop()
            print(next_node.value)
            if next_node.left != None:
                queue.insert(0, next_node.left)
            if next_node.right != None:
                queue.insert(0, next_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = []

        stack.append(self)

        while len(stack) > 0:
            curr_node = stack.pop()
            print(curr_node.value)
            if curr_node.right != None:
                stack.append(curr_node.right)
            if curr_node.left != None:
                stack.append(curr_node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left != None:
            self.left.pre_order_dft()
        if self.right != None:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left != None:
            self.left.post_order_dft()
        if self.right != None:
            self.right.post_order_dft()
        print(self.value)

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)


print("\nbreadth first")
bst.bft_print()

print("\ndepth first")
bst.dft_print()

print("\npre order")
bst.pre_order_dft()

print("\nin order")
bst.in_order_print()

print("\npost order")
bst.post_order_dft()
