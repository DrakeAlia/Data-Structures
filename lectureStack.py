# From lecture:
# List implementation
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = 
#     def __len__(self):
#         return len(self.storage)
#     def push(self, value):
#         # self.storage.insert(0, value) # O(n)
#         self.storage.append(value) # O(1)
#     def pop(self):
#         if len(self.storage) > 0:
#             return self.storage.pop() # O(1)
#         return None
# from singly_linked_list import LinkedList
# Linked List implementation
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
# ​
#     def __len__(self):
#         return self.size
# ​
#     def push(self, value):
#         self.storage.add_to_head(value) # O(1)
#         # self.storage.add_to_tail(value) # O(1)
#         self.size += 1
# ​
#     def pop(self):
#         if self.size > 0:
#             self.size -= 1
#             # return self.storage.remove_tail() # O(n)
#             return self.storage.remove_head() # O(1)
#         return None