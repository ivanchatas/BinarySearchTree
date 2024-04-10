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
    print(f'({node.key})', end='')
    if node.left is not None:
        printBST_preOrder(node.left)
    if node.right is not None:
        printBST_preOrder(node.right)


# A utility function to print
# the tree with the parent node from the BST postOrder
def printBST_postOrder(node):
    if node.left is not None:
        printBST_postOrder(node.left)
    if node.right is not None:
        printBST_postOrder(node.right)
    print(f'({node.key})', end='')


# A utility function to print
# the tree with the parent node from the BST inOrder
def printBST_inOrder(node):
    if node.left is not None:
        printBST_inOrder(node.left)
    print(f'({node.key})', end='')
    if node.right is not None:
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

def delete_node(root, key):
    # if root doesn't exist, just return it
    if not root:
        return root
    # Find the node in the left subtree	if key value is less than root value
    if root.key > key:
        root.left = delete_node(root.left, key)
    # Find the node in right subtree if key value is greater than root value,
    elif root.key < key:
	    root.right = delete_node(root.right, key)
	# Delete the node if root.keyue == key
    else:
        # If there is no right children delete the node and new root would be root.left
        if not root.right:
            return root.left
        # If there is no left children delete the node and new root would be root.right
        if not root.left:
            return root.right
  
        # If both left and right children exist in the node replace its value with
        # the minmimum value in the right subtree. Now delete that minimum node
        # in the right subtree
        temp_val = root.right
        mini_val = temp_val.key
        while temp_val.left:
            temp_val = temp_val.left
            mini_val = temp_val.key
        
        # Delete the minimum node in right subtree
        root.right = delete_node(root.right, root.key)
    return root