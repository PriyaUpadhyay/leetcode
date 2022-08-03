class Node:
    def __init__(self,start,end):
        self.start = start
        self.end  = end
        self.left = None
        self.right  = None
        
    def addNode(self,node):
        # going to the left
        if node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            else:
                return self.left.addNode(node)
        elif node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            else:
                return self.right.addNode(node)
        else:
            return False
            

class MyCalendar:

    def __init__(self):
        self.root = None
        

    def book(self, start: int, end: int) -> bool:
        if not self.root:
            self.root = Node(start,end)
            return True
        else:
            return self.root.addNode(Node(start,end))
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
