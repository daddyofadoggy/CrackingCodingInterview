# https://leetcode.com/problems/course-schedule/?envType=problem-list-v2&envId=topological-sort

from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.WHITE = 0
        self.GREY = 1
        self.BLACK = 2

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list = defaultdict(list)
        for dst, src in prerequisites:
            adj_list[src].append(dst)
        color = [self.WHITE] * numCourses

        def dfs(node):
            if color[node] == self.GREY:
                return False
            if color[node] == self.BLACK:
                return True
            # visit the node
            color[node] = self.GREY
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if not dfs(neighbor):
                        return False
            color[node] = self.BLACK
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        # Time and space complexity O(m+n) m is # edges and n is #nodes
