class Stack:
    def __init__(self, ml, lm):
        self.stack = ml
        self.limit = lm

    def pop(self):
        n = self.stack.pop()
        print(n)
        return n

    def push(self, el):
        if len(self.stack) < self.limit:
            return self.stack.append(el)
        else:
            print("The stack is full!")

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.stack) == self.limit:
            return True
        else:
            return False
    
    def getTop(self):
        return self.stack[-1]


    def __str__(self):
        return f"{self.stack}"
    
s1 = Stack([1,2,3,4,5], 7)
print(s1)
s1.pop()
s1.push(7)
print(s1.isEmpty())
print(s1.isFull())
print(s1.getTop())
print(s1)
