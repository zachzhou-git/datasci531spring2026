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


class Node:
    """A node of a linked list""" 

    def __init__(self, node_data):
        if type(node_data) in [type({}), type(()), type([])]:
            raise ValueError("data should not be a data structure")
        self._data = node_data 
        self._next = None 

    def get_data(self):
        """Get node data""" 
        return self._data 

    def set_data(self, node_data):
        """Set node data""" 
        if type(node_data) in [type({}), type(()), type([])]:
            raise ValueError("data should not be a data structure")
        self._data = node_data 

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node""" 
        return self._next 

    def set_next(self, node_next):
        """Set next node""" 
        self._next = node_next 
    
    next = property(get_next, set_next)

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return f"Node with value: {self._data}"