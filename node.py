# Python3 function to search a given key in a given BST

class Node:
	# Constructor to create a new node
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

# A utility function to print
# the tree with the parent node from the BST preOrder
def printBST_preOrder(node):
	print(f'({node.key})',end='')
	if node.left != None:
		printBST_preOrder(node.left)
	if node.right != None:
		printBST_preOrder(node.right)

# A utility function to print
# the tree with the parent node from the BST postOrder
def printBST_postOrder(node):
	if node.left != None:
		printBST_postOrder(node.left)
	if node.right != None:
		printBST_postOrder(node.right)
	print(f'({node.key})',end='')

# A utility function to print
# the tree with the parent node from the BST inOrder
def printBST_inOrder(node):
	if node.left != None:
		printBST_inOrder(node.left)
	print(f'({node.key})',end='')
	if node.right != None:
		printBST_inOrder(node.right)

# A utility function to insert
# a new node with the given key in BST
def insert(node, key):
	# If the tree is empty, return a new node
	if node is None:
		return Node(key)

	# Otherwise, recur down the tree
	if key < node.key:
		node.left = insert(node.left, key)
	elif key > node.key:
		node.right = insert(node.right, key)

	# Return the (unchanged) node pointer
	return node

# Utility function to search a key in a BST
def search(root, key):
	# Base Cases: root is null or key is present at root
	if root is None or root.key == key:
		return root

	# Key is greater than root's key
	if root.key < key:
		return search(root.right, key)

	# Key is smaller than root's key
	return search(root.left, key)
