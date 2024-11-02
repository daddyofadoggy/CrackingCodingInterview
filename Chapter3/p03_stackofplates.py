# https://leetcode.com/problems/dinner-plate-stacks/
class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.threshold = capacity
        self.arraystack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.arraystack) == 0:
            currentstack = []
            currentstack.insert(0, val)
            self.arraystack.append(currentstack)
            # self.threshold = self.threshold -1
        else:
            flag = 0
            for ars in self.arraystack:
                if len(ars) < self.threshold and flag == 0:
                    ars.insert(0, val)
                    flag = 1

            ## all sub stacks are full so create a new one
            if flag == 0:
                currentstack = []
                currentstack.insert(0, val)
                self.arraystack.append(currentstack)

        # print(self.arraystack)

    def pop(self):
        """
        :rtype: int
        """
        flag = 0
        # find the rightmost array with less capacity
        for i in range(len(self.arraystack) - 1, -1, -1):
            if len(self.arraystack[i]) > 0 and flag == 0:
                rightmost = self.arraystack[i]
                flag = 1
        ## if all the stack are empty return -1
        if flag == 0:
            return -1
        val = rightmost[0]
        rightmost.pop(0)
        # print(self.arraystack)
        return val

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if len(self.arraystack) < index:
            return -1
        arr = self.arraystack[index]
        if len(arr) == 0:
            return -1
        val = arr[0]
        arr.pop(0)
        # print(self.arraystack)
        return val

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)