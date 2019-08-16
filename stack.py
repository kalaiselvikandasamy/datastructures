class stack:
    def __init__(self):
        self.stack=[]
    def add(self,dataval):
        if dataval not in self.Stack:
            self.stack.append(dataval)
            return true
        else:
            return false
    def peek(self):
        return self.stack[-1]
    def push(self,data):
        self.stack.append(data)
        return self.stack
    def pop(self):
        if(len(self.stack))<=0:
            return("no element in stack")
        else:
            return self.stack.pop()
    def print(self):
        print(self.stack)
s=stack()
s.push('aishu')
s.push('dog')
print(s.peek())
s.push(True)
s.print()
s.pop()
