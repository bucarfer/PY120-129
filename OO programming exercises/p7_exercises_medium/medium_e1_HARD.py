'''### Exercise 1. Circular Buffer, *** HARD EXERCISE
A circular buffer is a collection of objects stored in a buffer that is treated as though it is connected end-to-end in a circle. When an object is added to this circular buffer, it is added to the position that immediately follows the most recently added object, while removing an object always removes the object that has been in the buffer the longest.

This works as long as there are empty spots in the buffer. If the buffer becomes full, adding a new object to the buffer requires getting rid of an existing object; with a circular buffer, the object that has been in the buffer the longest is discarded and replaced by the new object.

Assuming we have a circular buffer with room for 3 objects, the circular buffer looks and acts like this:

Your task is to write a CircularBuffer class in Python that implements a circular buffer for arbitrary objects. The class should be initialized with the buffer size and provide

the following methods:

put: Add an object to the buffer
get: Remove (and return) the oldest object in the buffer. Return None if the buffer is empty.

You may assume that none of the values stored in the buffer are None (however, None may be used to designate empty spots in the buffer).

'''

buffer = CircularBuffer(3)

print(buffer.get() is None)          # True

buffer.put(1)
buffer.put(2)
print(buffer.get() == 1)             # True

buffer.put(3)
buffer.put(4)
print(buffer.get() == 2)             # True

buffer.put(5)
buffer.put(6)
buffer.put(7)
print(buffer.get() == 5)             # True
print(buffer.get() == 6)             # True
print(buffer.get() == 7)             # True
print(buffer.get() is None)          # True

buffer2 = CircularBuffer(4)

print(buffer2.get() is None)         # True

buffer2.put(1)
buffer2.put(2)
print(buffer2.get() == 1)            # True

buffer2.put(3)
buffer2.put(4)
print(buffer2.get() == 2)            # True

buffer2.put(5)
buffer2.put(6)
buffer2.put(7)
print(buffer2.get() == 4)            # True
print(buffer2.get() == 5)            # True
print(buffer2.get() == 6)            # True
print(buffer2.get() == 7)            # True
print(buffer2.get() is None)         # True

# how to move objects from oldest to newest, 1st, 2nd and 3rd (1st oldest, 3rd newest)
# For put and use the order 1, 2, 3
    # -> if the three are empty return None
    # -> if the three are taken -> rewrite 1

### Solution

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.next = 0 # write pointer
        self.oldest = 0 # read pointer
        self.buffer_list = [None for _ in range(self.size)]

    def get(self):
        # if buffer is empty returns None
        if self.buffer_list[self.oldest] == None:
            return None
        # returns oldest value, resets that place to None and moves oldest by one with modulo
        else:
            get_value = self.buffer_list[self.oldest]
            self.buffer_list[self.oldest] = None
            self.oldest = (self.oldest + 1) % self.size
            return get_value

    def put(self, item):
        if self.buffer_list[self.next] != None:
            # first we move oldest one
            self.oldest = (self.oldest + 1) % self.size
        #write item in current next position
        self.buffer_list[self.next] = item
        #advance CircularBuffer to next position
        self.next = (self.next + 1) % self.size

    def check_list(self):
        return self.buffer_list


## LS solution (very similar)

class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size
        self.next = 0
        self.oldest = 0

    def put(self, obj):
        next_item = (self.next + 1) % len(self.buffer)

        if self.buffer[self.next] is not None:
            self.oldest = next_item

        self.buffer[self.next] = obj
        self.next = next_item

    def get(self):
        value = self.buffer[self.oldest]
        self.buffer[self.oldest] = None
        if value is not None:
            self.oldest += 1
            self.oldest %= len(self.buffer)

        return value