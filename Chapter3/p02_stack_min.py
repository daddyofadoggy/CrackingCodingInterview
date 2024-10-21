
class MinStack(object):

    def __init__(self):
        self.s1 = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        minimum = self.getMin()
        if minimum is None or val<minimum:
            minimum = val
        self.s1.insert(0,(val, minimum))

    def pop(self):
        """
        :rtype: None
        """
        self.s1.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.s1[0][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.s1) ==0 :
            return None
        return self.s1[0][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()