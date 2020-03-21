import AVLTree
import random

def value(node):
    if node:
        return node.val
    return None

def print_tree(root):
    if root:
        print((root.val,value(root.left),value(root.right)))
        print_tree(root.left)
        print_tree(root.right)

my_list = range(10)
random.shuffle(my_list)
tree = AVLTree.AVL_Tree()
root = None
for key in my_list:
    root = AVLTree.AVL_Tree.insert(tree,root,key)

print_tree(root)
print("break")
root = AVLTree.AVL_Tree.delete(tree,root,9)
print_tree(root)
print("break")
root = AVLTree.AVL_Tree.delete(tree,root,4)
print_tree(root)
print("break")
root = AVLTree.AVL_Tree.delete(tree,root,6)
print_tree(root)

