class RingBuffer:
    def __init__(self, capacity):
        #the set up
        self.capacity = capacity
        self.storage = [None] * capacity
        self.counter = 0
        
    def append(self, item):
        #makes the items
        self.storage[self.counter] = item
        #adds 1 to the conter
        self.counter += 1
        #if the counter and the cpacity is the same then dont change
        if self.counter == self.capacity:
            self.counter = 0
        else:
            #self.counter += 1
            pass
        
    def get(self):
        return [item for item in self.storage if item is not None]
        #it filters the storage and gets rid of the None in the list