
class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    # push
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()
    
    # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list)-1]
    
    # delete
    def delete(self):
        self.list = None




customStack = Stack()
print(customStack.isEmpty())
customStack.push(6)
customStack.push(4)
customStack.push(3)
print(customStack.peek())
# print(customStack.pop())
print(customStack)
