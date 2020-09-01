"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
"""
from copy import deepcopy

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
		if not root:
			return root

		if root.val > key:
			root.left = self.deleteNode(root.left, key)

		elif root.val < key:
			root.right = self.deleteNode(root.right, key)

		else:
			if not root.right:
				return root.left

			if not root.left:
				return root.right

			temp = root.right
			mini = temp.val
			while temp.left:
				temp = temp.left
				mini = temp.val

			root.val = mini
			root.right = self.deleteNode(root.right, root.val)

		return root



def traverse(root):
	if not root:
		return
	current_level = [root]
	while current_level:
		print(' '.join(str(node.val) for node in current_level))
		next_level = list()
		for n in current_level:
			if n.left:
				next_level.append(n.left)
			if n.right:
				next_level.append(n.right)
		current_level = next_level


if __name__ == '__main__':
	S = Solution()

	tree1 = TreeNode(5)
	tree1.left = TreeNode(3)
	tree1.right = TreeNode(6)
	tree1.left.left = TreeNode(2)
	tree1.left.right = TreeNode(4)
	tree1.right.right = TreeNode(7)

	new_tree = S.deleteNode(deepcopy(tree1), 3)

	print('Original: ')
	traverse(tree1)
	print()
	print('New:')
	traverse(new_tree)
