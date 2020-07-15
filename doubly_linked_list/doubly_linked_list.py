"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
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
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # create instance of ListNode with value
        # increment the DLL length attribute
        new_node = ListNode(value)
        self.length += 1

        # if DLL is empty
            # set head and tail to the new node instance
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # if DLL is not empty
            # set new node's next to current head
            # set head's prev to new node
            # set head to the new node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # store the value of the head
        # decrement the length of the DLL
        self.length -= 1
        # delete the head
        # if head.next is not None
        if self.head.next != None:
            # set head.next's prev to None
            self.head.next.prev = None
            # set head to head.next
            self.head =  self.head.next
            return self.head.value
        # else (if head.next is None)
        else:
            # set head to None
            # set tail to None
            self.head = None
            self.tail= None
            return None
        # return the value
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
        if self.length == 0:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        # if DLL is not empty
        else:
            # set new node's prev to current tail
            new_node.prev = self.tail
            # set tail's next to new node
            self.tail.next = new_node
            # set tail to the new node
            self.tail = new_node
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is self.head:
            return self.head

        elif node is self.tail:
            node.next = self.head
            self.head.prev = self.tail
            self.head = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is self.head:
            tail = self.tail
            self.head = node.next
            self.head.prev = None
            self.tail.next = node
            self.tail = node
            self.tail.next = None
            self.tail.prev = tail
        elif node is self.tail:
            return self.tail

        else:
            current = self.head
            while current:
                if current == node:
                    previous_node = current.prev
                    next_node = current.next
                    previous_node.next = next_node
                    next_node.prev = previous_node
                    current.next = None
                    current.prev = None
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                    self.tail.next = None
                current = current.next
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head and not self.tail:
            return None

        self.length -= 1
        if self.head is self.tail:
            self.head = None
            self.tail = None

        elif self.head == node:
            self.head = node.next
            node.delete()
            
        elif self.tail == node:
            self.tail = node.prev
            node.delete()

        else:
            node.delete()
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            else:
                current = current.next
        return max_value