# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compare(self, left, right) -> bool:
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        elif left.left == None and left.right == None and right.left == None and right.right == None:
            return left.val == right.val
        else:
            if left.val != right.val:
                return False
            result = self.compare(left.left, right.right) and self.compare(left.right, right.left)
        
            return result
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compare(root.left, root.right)