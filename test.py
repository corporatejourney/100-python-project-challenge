class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        else:
            return self.items.pop()
        
stack = Stack()
stack.push(1)
stack.push(3)
stack.is_empty()
stack.pop()

print(stack.pop())
print(stack.is_empty())
print(stack.pop())