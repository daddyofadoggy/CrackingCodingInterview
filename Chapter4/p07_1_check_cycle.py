from collections import defaultdict


class Solution(object):
    def __init__(self):
        self.WHITE = 0
        self.GREY = 1
        self.BLACK = 2
        self.is_no_cycle = True

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        color = [self.WHITE] * numCourses
        dic = defaultdict(list)
        for dst, src in prerequisites:
            dic[src].append(dst)

        def dfs(vertex):
            if not self.is_no_cycle:
                return
            color[vertex] = self.GREY

            if vertex in dic:
                for node in dic[vertex]:
                    if color[node] == self.WHITE:
                        dfs(node)
                    if color[node] == self.GREY:
                        self.is_no_cycle = False
            # end of recursion
            color[vertex] = self.BLACK
            # topological_order.append(vertex)

        for node in range(numCourses):
            if color[node] == self.WHITE:
                dfs(node)
        return self.is_no_cycle
        # Time and space complexity O(m+n) m is # edges and n is #nodes