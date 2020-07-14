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
from singly_linked_list import Node , LinkedList

# Array Implementation
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         return self.storage.insert(0,value)

#     def dequeue(self):
#         if len(self.storage)==0:
#             pass
#         else:
#             return self.storage.pop()


# Linked List Implementation

class Queue:
    def __init__(self):
        self.size = 0
        self.front = None
        self.back = None
    def __len__(self):
        return self.size

    def enqueue(self, value):
        queued = Node(value)
        if self.back == None:
            self.size += 1
            self.front = queued
            self.back = queued
        else:
            self.size += 1
            self.back.next_node = queued
            self.back = queued

    def dequeue(self):
        if self.front== None:
            return None
        else:
            self.size -= 1
            dequeued = self.front
            self.front = dequeued.next_node
            return dequeued.value