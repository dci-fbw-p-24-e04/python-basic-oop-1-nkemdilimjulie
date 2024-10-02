# '''

# """ Queue may be implemented with Lists just as Stacks. But deque are preferred
# because they allowed optimized accessing/deleting from both ends.

# Deleting from the front of a list is O(n) as all other elements need to be shifted

# Also, with deque, we can implement double-ended Queues.""" '''


# from collections import deque


# class Queue:
#     def __init__(self):
#         self._data = self.deque()

#     def is_empty(self):
#         # TODO: Replace 'pass' with your code
#         pass

#     @property
#     def size(self):
#         # TODO: Replace 'pass' with your code
#         pass

#     def enqueue(self, item):
#         self.item = item
#         # TODO: Replace 'pass' with your code
#         pass

#     def peek(self):
#         # TODO: Replace 'pass' with your code
#         pass

#     def dequeue(self):
#         # TODO: Replace 'pass' with your code
#         pass

#     def __str__(self) -> str:
#         return str(self._data)


# if __name__ == "__main__":
#     q = Queue()
#     q.enqueue(0)
#     q.enqueue(1)
#     print(q)
#     print("Size of Queue: ", q.size)
#     print("Peek the Queue: ", q.peek())
#     print("Pop from Queue: ", q.dequeue())
#     print("Peek the Queue: ", q.peek())
#     print("Size of Queue: ", q.size)
#     print("Pop from Queue: ", q.dequeue())
#     print("Size of Queue: ", q.size)
#     print("Peek the Queue: ", q.peek())

'''

""" Queue may be implemented with Lists just as Stacks. But deque are preferred
because they allowed optimized accessing/deleting from both ends.

Deleting from the front of a list is O(n) as all other elements need to be shifted

Also, with deque, we can implement double-ended Queues.""" '''


from collections import deque


class Queue:
    def __init__(self):
        self._data = [ ]
        self._data.append('e')
        self._data = self.dequeue()

    def is_empty(self):
        if len(self._data) == 0:
            return True
        else:
            return False

    @property
    def size(self):
        return len(self._data)

    def enqueue(self, item):
        self.item = item
       
        self._data.append(self.item)

    def peek(self):
        if self.is_empty():
            raise 'Exception ---> Queue is empty'
        return f'The element at the front of the queue is {self._data[0]}'

    def dequeue(self):
      if self.is_empty():
        raise 'Exception ---> Queue is empty'
      print(f'The element at the front of the queue is {self._data[0]}')
      del self._data[0]

    def __str__(self):
        return str(self._data)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(0)
    q.enqueue(1)
    print(q)
    print("Size of Queue: ", q.size)
    print("Peek the Queue: ", q.peek())
    print("Pop from Queue: ", q.dequeue())
    print("Peek the Queue: ", q.peek())
    print("Size of Queue: ", q.size)
    print("Pop from Queue: ", q.dequeue())
    print("Size of Queue: ", q.size)
    print("Peek the Queue: ", q.peek())