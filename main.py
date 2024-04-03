import node

# Driver Code
if __name__ == '__main__':
	root = None
	root = node.insert(root, 50)
	node.insert(root, 30)
	node.insert(root, 20)
	node.insert(root, 40)
	node.insert(root, 70)
	node.insert(root, 60)
	node.insert(root, 80)

	# Key to be found
	key = 6

	# Searching in a BST
	if node.search(root, key) is None:
		print(key, "not found")
	else:
		print(key, "found")

	key = 60

	# Searching in a BST
	if node.search(root, key) is None:
		print(key, "not found")
	else:
		print(key, "found")

	node.printBST_preOrder(root)
	node.printBST_postOrder(root)
	node.printBST_inOrder(root)
