#A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. 
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.store = [None]*capacity
        self.now = 0

#The append method adds the given element to the buffer
    def append(self, item):
        self.store[self.now] = item
        self.now += 1
        if self.now == self.capacity:
            self.now = 0

#The get method returns all of the elements in the buffer in a list in their given order.
    def get(self):
        return [newvalue for newvalue in self.store if newvalue is not None]