# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #p: Optional[TreeNode], q: Optional[TreeNode]
    def isSameTree(self, p, q) -> bool:
        # if both trees are empty, we made it to the end without discrepencies
        if not p and not q:
            return True
        
        # edge cases: one tree is empty while the other has a value or the values !=
        if not p or not q or p.val != q.val:
            return False

        # if the current branch for each side matches, check subsequent branches
        return self.isSameTree(p.left, q.left) and \
               self.isSameTree(p.right, q.right)
