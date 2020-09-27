"""
Given two binary search trees root1 and root2.

Return a list containing all the integers from both trees sorted in ascending order.

Example 1:
Input: root1 = [2,1,4], root2 = [1,0,3]
Output: [0,1,1,2,3,4]

Example 2:
Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
Output: [-10,0,0,1,2,5,7,10]

Example 3:
Input: root1 = [], root2 = [5,1,7,0,2]
Output: [0,1,2,5,7]

Example 4:
Input: root1 = [0,-10,10], root2 = []
Output: [-10,0,10]

Example 5:
Input: root1 = [1,null,8], root2 = [8,1]
Output: [1,1,8,8]


Constraints:
Each tree has at most 5000 nodes.
Each node's value is between [-10^5, 10^5].
"""
from typing import List


class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
		self.element_list = []

		self.__get_tree_elements(root1)
		self.__get_tree_elements(root2)

		return sorted(self.element_list)

	def __get_tree_elements(self, node: TreeNode):
		if not node:
			return

		self.__get_tree_elements(node.left)
		self.element_list.append(node.val)
		self.__get_tree_elements(node.right)

	def __traverse(self, root: TreeNode):
		if not root:
			return

		current_level = [root]
		while current_level:
			yield [node.val for node in current_level]
			next_level = list()
			for n in current_level:
				if n.left:
					next_level.append(n.left)
				if n.right:
					next_level.append(n.right)
			current_level = next_level


if __name__ == '__main__':
	S = Solution()

	tree1 = TreeNode(2)
	tree1.left = TreeNode(1)
	tree1.right = TreeNode(4)

	tree2 = TreeNode(1)
	tree2.left = TreeNode(0)
	tree2.right = TreeNode(3)

	print('[0,1,1,2,3,4] -> ', S.getAllElements(tree1, tree2))
