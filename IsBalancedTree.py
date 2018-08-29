# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        return self.dfs(pRoot) != -1
    def dfs(self, p):
        if p is None:
            return 0
        l = self.dfs(p.left)
        if l == -1:
            return -1
        r = self.dfs(p.right)
        if r == -1:
            return -1
        if abs(l - r) > 1:
            return -1
        return max(l, r) + 1
