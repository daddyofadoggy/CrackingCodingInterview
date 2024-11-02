# https://leetcode.com/problems/course-schedule-ii/description/

from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.WHITE = 0
        self.GREY = 1
        self.BLACK = 2
        self.is_possible = True

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        color = [self.WHITE] * numCourses
        dic = defaultdict(list)
        for dst, src in prerequisites:
            dic[src].append(dst)
        topological_order = []

        def dfs(vertex):
            if not self.is_possible:
                return
            color[vertex] = self.GREY

            if vertex in dic:
                for node in dic[vertex]:
                    if color[node] == self.WHITE:
                        dfs(node)
                    if color[node] == self.GREY:
                        self.is_possible = False
            # end of recursion
            color[vertex] = self.BLACK
            topological_order.append(vertex)

        for node in range(numCourses):
            if color[node] == self.WHITE:
                dfs(node)
        return topological_order[::-1] if self.is_possible else []
