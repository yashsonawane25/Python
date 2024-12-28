class PriorityQueue:
    def __init__(self):
        self.items=[]
    def push(self,data,priority):
        index =0
        while index<len(self.items) and self.items[index][1] <=priority:
             index+=1
        self.items.insert(index,(data,priority))
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        return self.items.pop(0)[0]
    def size(self):
        return len(self.items)
p=PriorityQueue()
p.push("Amit",4)
p.push("Ajay",7)
p.push("ashima",2)
p.push("Amit",5)
p.push("Amit",1)
p.push("Amit",8)
p.push("Amit",4)

while not p.is_empty():
    print(p.pop())