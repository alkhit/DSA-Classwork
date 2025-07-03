class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top is None
    
    def push(self, value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty stack")
        
        popped = self.top.value
        self.top = self.top.next
        return popped
    
    def peek(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        
        return self.top.value
    
    def display(self):
        current = self.top
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print("Stack from top to bottom: ","->".join(values))

if __name__ == "__main__":
    sll = LinkedListStack()
    sll.push(5)
    sll.push(10)
    sll.push(15)
    sll.display()

    print("Peek top: ", sll.peek())
    print("Pop result: ", sll.pop())
    sll.display()    
