"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        self.next
        
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
        head_value = self.head.value
        # decrement the length of the DLL
        self.length -= 1
        # delete the head
        # if head.next is not None
        if self.head.next is not None:
            # set head.next's prev to None
            self.head.next.prev = None
            # set head to head.next
            self.head =  self.head.next
        # else (if head.next is None)
        else:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None
        # return the value
        return head_value
            
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
        # store the value of the tail
        tail_value = self.tail.value
        # decrement the length of the DLL
        self.length -= 1
        # delete the tail
        # if tail.prev is not None
        if self.tail.prev is not None:
            # set tail.prev's next to None
            self.tail.prev.next = None
            # set tail to tail.prev
            self.tail = self.tail.prev
        # else (if tail.prev is None)
        else:
            # set head to None
            self.head = None
            # set tail to None
            self.tail = None
        # return the value
        return tail_value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass