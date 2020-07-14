# From Lecture:
# List implementation
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = 
#     def __len__(self):
#         return len(self.storage)
#     def enqueue(self, value):
#         # self.storage.append(value) # O(1)
#         self.storage.insert(0, value) # O(n)
#     def dequeue(self):
#         if len(self.storage) > 0:
#             # return self.storage.pop(0) # O(n)
#             return self.storage.pop() # O(1)
#         return None
# from singly_linked_list import LinkedList
# Linked List implementation
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()   
#     def __len__(self):
#         return self.size
# ​
#     def enqueue(self, value):
#         self.storage.add_to_tail(value) # O(1)
#         self.size += 1
# ​
#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.remove_head() # O(1)
#         return None