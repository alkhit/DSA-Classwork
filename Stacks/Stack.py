stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushes: ", stack)

top_element = stack[-1]
print("Top element: ", top_element)

if len(stack) == 0:
    print("The stack is empty")
else:
    print("Stack has values")

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def peek(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        return self.items[-1]
    
    def pop(self):
        if self.isEmpty():
            raise Exception("The stack is empty")
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    
    def print(self):
        print("The stack from top to bottom: ", self.items)
        return
    
if __name__ == "__main__":
    s1 =Stack()
    s1.push(300)
    s1.push(350)
    s1.push(400)

    s1.print()
    
    print("Top element: ", s1.peek())
    print("Popped: ", s1.pop())

    print("Is stack empty? ", s1.isEmpty())

    s1.pop()
    s1.pop()
    print("Is stack empty now? ", s1.isEmpty())
