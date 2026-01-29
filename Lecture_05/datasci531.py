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