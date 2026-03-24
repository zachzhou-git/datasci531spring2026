### Add BinaryTree class after lecture_18_a_tree_traversal.ipynb

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