# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
      #DFS解法: 过一遍整个binary tree所有nodes, record levels, 
        sum = [] #先设计算每层node sum, 里面也有sum[level]记层数
        def dfs(node: TreeNode, level: int) -> None: #这是dynamic array, name: type定义
            if level == len(sum): #If reach the last level, append node values to sum 
                sum.append(node.val)
            else:
                sum[level] += node.val #if not reach last level, add node value to its level's sum
            if node.left: #if node exists on left or right, level+1
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
        dfs(root, 0)
        return sum.index(max(sum)) + 1

