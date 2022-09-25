"""
Implement Queue using Stacks
Grind 75 #14
LC # 232 Easy

Solution:
time complexity is amortized O(1)
space complexity is O(n)? - for amount of items entered into stack, maybe
"""


class MyQueue:

    def __init__(self):
        self.input = []
        
    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        res = self.input[-len(self.input)]
        del self.input[-len(self.input)]
        return res

    def peek(self) -> int:
        return self.input[-(len(self.input))]

    def empty(self) -> bool:
        return len(self.input) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()