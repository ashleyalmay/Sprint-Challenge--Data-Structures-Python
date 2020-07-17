class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.counter = 0
        
    def append(self, item):
        self.storage[self.counter] = item
        self.counter += 1
        if self.counter == self.capacity:
            self.counter = 0
        else:
            #self.counter += 1
            pass
        
    def get(self):
        return [item for item in self.storage if item is not None]