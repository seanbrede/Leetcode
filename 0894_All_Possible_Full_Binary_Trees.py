# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        # no possible trees of even size
        if n % 2 == 0: return []

        # base case is a single node
        possible_trees = {1: [TreeNode()]}

        # iterate over all possible tree sizes
        for size in range(3, n + 1, 2):
            possible_trees[size] = []

            # iterate over all possible sizes of left and right subtrees for the root node
            for left_size in range(1, size - 1, 2):
                right_size = size - left_size - 1
                for left_side in possible_trees[left_size]:
                    for right_side in possible_trees[right_size]:
                        # create root nodes with each possible configuration of left and right subtree
                        possible_trees[size].append(TreeNode(left=left_side, right=right_side))

        return possible_trees[n]
