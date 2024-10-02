
class Stack:
    """ This is reliable because it uses; append and pop which have O(1) """

    def __init__(self):
        self._data = [ ]

    def push(self, item):
        self.item = item
        """ Add item to the top of the stack """
        self._data.append(self.item)
              
    def peek(self):
        """ Show the item at the top of the stack without removing it """
        if self.is_empty():
            raise 'Exception -- stack is empty'
        top_item = self._data[-1]
        return f'The item at the top is {top_item}'

    def is_empty(self):
        """Return True if the stack is empty"""
        if len(self._data) == 0:
            return True
        else:
            return False

    def size(self):
        """Return the size of the stack"""
        total_item = len(self._data)
        return f'size of items in a stack are {total_item}'

    def pop(self):
        """ Remove and return the item at the top of the stack """
        if self.is_empty():
            raise 'Exception -- stack is empty'
        self._data.pop()
        return f'remaining items after removal of the last item: {self._data}'

if __name__ == "__main__":
    s = Stack()
    print("Is empty? ", s.is_empty())
    print("Pushed 4")
    s.push(4)
    print("Peek top: ", s.peek())
    print("Pushed 5")
    s.push(5)
    print("Peek top: ", s.peek())
    print("Is empty? ", s.is_empty())
    print("Size is: ", s.size())
    print("Pop from top: ", s.pop())
    print("Size is: ", s.size())
    print("Peek top: ", s.peek())
    print("Pop from top: ", s.pop())
    print("Size is: ", s.size())
    print("Is empty? ", s.is_empty())
