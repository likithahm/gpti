import time
start=time.time()
class stack:
   def __init__(self):
     self.items=[]
   def isEmpty(self):
     return self.items ==[]
   def push(self,item):
       self.items.append(item)
       print(item)
   def pop(self):
     return self.items.pop()
   def peek(self):
     return self.items[len(self.items)-1]
   def size(self):
     return len(self.items)
s=stack()
print(s.isEmpty())
print("push")
s.push(11)
s.push(12)
s.push(13)
print("peek",s.peek())
print("pop")
print(s.pop())
print(s.pop())
print("size",s.size())
end=time.time()
print(f"runtime of the program is{end-start}")

