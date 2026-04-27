### Add BinaryTree class after lecture_18_a_tree_traversal.ipynb
class BinaryTree:
    def __init__(self, root_val):
        self.key = root_val
        self.left_child = None 
        self.right_child = None

    def insert_left(self, new_item):
        if self.left_child is None:
            self.left_child = BinaryTree(new_item)
        else:
            new_child = BinaryTree(new_item)
            new_child.left_child = self.left_child 
            self.left_child = new_child
    
    def insert_right(self, new_item):
        if self.right_child is None:
            self.right_child = BinaryTree(new_item)
        else:
            new_child = BinaryTree(new_item)
            new_child.right_child = self.right_child 
            self.right_child = new_child 

    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()

    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.key)
        if self.right_child:
            self.right_child.inorder()

    def postorder(self):
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()

        print(self.key)

    def get_root_val(self):
        return self.key 

    def set_root_val(self, new_val):
        self.key = new_val 

    def get_left_child(self):
        return self.left_child 
    
    def get_right_child(self):
        return self.right_child

    def __str__(self):
        return f"BinaryTree with root value {self.key}"

    def __repr__(self):
        return f"BinaryTree with root value {self.key}"

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