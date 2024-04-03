# Binary Search Tree(BST)

Binary search tree is a data structure that quickly allows us to maintain a sorted list of numbers.

* It is called a binary tree because each tree node has a maximum of two children.
* It is called a search tree because it can be used to search for the presence of a number in O(log(n)) time.

The properties that separate a binary search tree from a regular binary tree is

  1. All nodes of left subtree are less than the root node
  2. All nodes of right subtree are more than the root node
  3. Both subtrees of each node are also BSTs i.e. they have the above two properties
