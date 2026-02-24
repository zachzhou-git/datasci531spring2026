class Stack:
    # Implementation of a Stack
    # Bottom of Stack is at beginning of list (position 0)
    # Top of Stack is at end of list (position -1)

    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()
    
    def peek(self):
        return self._items[-1]

    def size(self):
        return len(self._items)


class Queue:
    # Implementation of a Queue using Python list
    # Rear of queue is at beginning of list (position 0)
    # Front of queue is at end of list (position -1)

    def __init__(self):
        # initialize empty queue
        self._items = []

    def is_empty(self):
        # same as Stack
        return not bool(self._items)

    def enqueue(self, item):
        # Adds item to queue (at the rear)
        # Uses .insert method at position 0
        # No value is returned
        self._items.insert(0, item)

    def dequeue(self):
        # Remove item from queue (at the front)
        return self._items.pop()

    def size(self):
        # same as Stack
        return len(self._items)

class Deque:
    """Deque implementation as a list"""

    def __init__(self):
        """Create new deque"""
        self._items = []

    def is_empty(self):
        """Check if the deque is empty"""
        return not bool(self._items)

    def add_front(self, item):
        """Add an item to the front of the deque"""
        self._items.append(item)

    def add_rear(self, item):
        """Add an item to the rear of the deque"""
        self._items.insert(0, item)

    def remove_front(self):
        """Remove an item from the front of the deque"""
        return self._items.pop()

    def remove_rear(self):
        """Remove an item from the rear of the deque"""
        return self._items.pop(0)

    def size(self):
        """Get the number of items in the deque"""
        return len(self._items)


class Node:
    """A node of a linked list""" 

    def __init__(self, node_data):
        if type(node_data) in [type({}), type(()), type([])]:
            raise ValueError("data should not be a data structure")
        self._data = node_data 
        self._next = None 

    @property 
    def data(self):
        """Get node data""" 
        return self._data 

    @data.setter
    def data(self, node_data):
        """Set node data""" 
        if type(node_data) in [type({}), type(()), type([])]:
            raise ValueError("data should not be a data structure")
        self._data = node_data 

    @property
    def next(self):
        """Get next node""" 
        return self._next 

    @next.setter 
    def next(self, node_next):
        """Set next node"""
        # should write test to make sure "node_next" is a node 
        if type(node_next) != type(self):
            raise ValueError("next should be another Node!")
        self._next = node_next 

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return f"Node with value: {self._data}" 