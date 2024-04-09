import node

def default_code():
	root = None
	root = node.insert(root, 50)
	node.insert(root, 30)
	node.insert(root, 20)
	node.insert(root, 40)
	node.insert(root, 70)
	node.insert(root, 80)
	node.insert(root, 60)
	return root

def menu(root):
	print('\n******************************')
	print('***          MENU          ***')
	print('******************************')
	print('***   1. Add new value     ***')
	print('***   2. Search a value    ***')
	print('***   3. Delete a value    ***')
	print('***   4. Print pre-order   ***')
	print('***   5. Print in-order    ***')
	print('***   6. Print post-order  ***')
	print('***   7. Default example   ***')
	print('***                        ***')
	print('******************************')
	opt = int(input('Choose an option: '))
	match opt:
		case 1:
			val = int(input('Enter a value to add: '))
			if root is None:
				root = node.insert(root, val)
			else:
				node.insert(root, val)
		case 2:
			key = int(input('Enter a value to search: '))
			if node.search(root, key) is None:
				print(key, "not found")
			else:
				print(key, "found")
		case 3:
			val = int(input('Enter a value to delete: '))
			node.delete_node(root, val)
		case 4:
			if root is None:
				print("The structure is empty")
			else:
				node.printBST_preOrder(root)
		case 5:
			if root is None:
				print("The structure is empty")
			else:
				node.printBST_inOrder(root)
		case 6:
			if root is None:
				print("The structure is empty")
			else:
				node.printBST_postOrder(root)
		case 7:
			root = default_code()
		case _:
			print("Please enter an exist option")
	
	menu(root)

root = None
menu(root)
