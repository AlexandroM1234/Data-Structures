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
from singly_linked_list import Node , LinkedList

# List Implementation
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) == 0:
#             pass
#         else:
#             return self.storage.pop()


# Linked List Implementation
class Stack:
    def __init__(self):
        self.size = 0
        self.head = None

    def __len__(self):
        return self.size

    def push(self, value):
        if self.head == None:
            self.size += 1
            self.head = Node(value)
        else:
            self.size += 1
            new_node = Node(value)
            new_node.set_next=self.head
            self.head = new_node

    def pop(self):
        if self.size == 0:
            pass
        else:
            self.size -= 1
            popped_node = self.head
            new_head = popped_node.next_node
            self.head = new_head
            return self.head