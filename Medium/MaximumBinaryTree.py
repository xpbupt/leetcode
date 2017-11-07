'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note:
The size of the given array will be in the range [1,1000].
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        # max_v, max_idx = self.find_index_and_max_num(nums)
        max_v = max(nums)
        max_idx = nums.index(max_v)
        tree_node = TreeNode(max_v)
        tree_node.left = self.constructMaximumBinaryTree(nums[:max_idx])
        tree_node.right = self.constructMaximumBinaryTree(nums[max_idx+1:])
        return tree_node


    def find_index_and_max_num(self, nums):
        max_v = 0
        max_idx = 0
        for i in range(len(nums)):
            if nums[i] >= max_v:
                max_v = nums[i]
                max_idx = i
        return max_idx, max_v       
