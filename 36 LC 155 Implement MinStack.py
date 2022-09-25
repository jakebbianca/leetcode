"""
Implement MinStack
Grind 75 #36
LC #155 Medium
"""


class MinStack:

    def __init__(self):
        self.stack = []

    # we will use tuples to add value as well as min value at given point in the stack
    # first value is input, second value is min at that point
    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val, min(val, self.stack[-1][1])))
        else:
            self.stack.append((val, val))
        

    # program spec says to return None, so not returning popped val
    # if there is an item in the stack, delete last item in the stack
    def pop(self) -> None:
        if self.stack:
            del self.stack[-1]
        else:
            return
        
    # return last input val
    def top(self) -> int:
        return self.stack[-1][0]

    # return min at last stack index
    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()














