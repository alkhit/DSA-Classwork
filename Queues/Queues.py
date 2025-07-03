class CircularQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * CircularQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0 

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size ==0
    
    def first(self):
        if self.isEmpty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def enqueue(self,element):
        if self._size == len(self._data):
            self._resize(2* len(self._data))
        
        tail = (self._front+ self._size)% len(self._data)
        self._data[tail]= element
        self._size +=1

    def deque(self):
        if self.isEmpty():
            raise Empty('Queue is empty')
        
        dequeued_element = self._data[self._front]
        self._data[self._front] = None
        self._front =(self._front +1)% len(self._data)
        self._size -= 1

        return dequeued_element
    
    def _resize(self, new_capacity):
        old_data = self._data
        new_data = [None] * new_capacity
        walk = self._front
        for k in range(self._size):
            new_data[k] = old_data[walk]
            walk = (walk +1)% len(old_data)

        self._data = new_data
        self._front = 0

    def print_queue(self):
        result = []
        index = self._front
        for i in range(self._size):
            result.append(str(self._data[index]))
            index = (index + 1) % len(self._data)
        print("Queue from front to rear:", " -> ".join(result))

class Empty(Exception):
    pass

if __name__ == '__main__':
    q= CircularQueue()
    insert_elements = [11,22,33,44,55]

    for element in insert_elements:
        q.enqueue(element)

        print(f"Added element: {element}")
        print(f"The new size of queue is {len(q)}")

    print("\n Current Queue representation: ")
    q.print_queue()



