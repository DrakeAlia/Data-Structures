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
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass




"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

#Linked List Implementation
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
    def __init__(self):
        # Array Implementation
        # self.storage = []

        # Linked List Implementation
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        # Array Implementation
        # return len(self.storage)

        # Linked List Implementation
        # Start at the head and add one to the count until you reach the tail (.next is None)
        return self.size

    def push(self, value):
        # Array Implementation
        # self.storage.append(value)

        # Linked List Implementation
        new_node = Node(value)
        # If the list is empty, set the head node and it's .next value to be the value
        if self.head is None:
            self.head = new_node
            # self.head.next = new_node
            self.tail = new_node
        # Otherwise, if there are nodes, change the current tail's .next value from None to the value
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def pop(self):
        # Array Implementation
        # if len(self.storage) == 0:
        #     return None
        # else:
        #     value = self.storage.pop()
        #     return value
        
        # Linked List Implementation
        if self.head is None:
            return None
        elif self.head.next is None:
            removed = self.head
            self.head = None
            self.size -= 1
            return removed.data
        else:
            new_last = self.head
            # While there is at least two elements after the current Node, keep moving through the loop since it isn't the next to last Node
            while new_last.next.next:
                new_last = new_last.next

            removed = new_last.next
            new_last.next = None
            self.size -= 1
            return removed.data