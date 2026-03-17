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
        if type(node_next) != type(self) and type(node_next) != type(None):
            raise ValueError("next should be another Node!")
        self._next = node_next 

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return f"Node with value: {self._data}" 