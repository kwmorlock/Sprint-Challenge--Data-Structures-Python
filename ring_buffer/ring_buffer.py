#A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. 
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = []
        self.index = -1

#The append method adds the given element to the buffer
    def append(self, item):
        pass

#The get method returns all of the elements in the buffer in a list in their given order.
    def get(self):
        pass