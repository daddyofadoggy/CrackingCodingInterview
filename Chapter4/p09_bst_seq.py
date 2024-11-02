# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
class Solution(object):
    def comb(self ,nl ,nr):
        return self.factorial[n l +nr] // self.factorial[nl ]// self.factorial[nr]
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mod = 1 0* *9 + 7
        m = len(nums)
        n = len(nums)
        self.factorial = [1 ] *n
        for i in range(1 ,n):
            self.factorial[i] = i * self.factorial[ i -1]

        def dfs(nums):
            m = len(nums)
            if m< 3:
                return 1
            left = [a for a in nums if a < nums[0]]
            right = [a for a in nums if a > nums[0]]

            return self.comb(len(left), len(right)) * dfs(left) * dfs(right)

        return (dfs(nums) - 1) % mod
