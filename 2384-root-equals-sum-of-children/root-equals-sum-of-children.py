# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # if not root or not root.left or not root.right:
            # return False # or raise error

        #return root.val == root.left.val + root.right.val
        
        left_val = root.left.val
        right_val = root.right.val
        root_val = root.val

        print("root:", root_val, "left:", left_val, "right:", right_val)
        print("left + right:", left_val + right_val)

        return root_val == left_val + right_val
        