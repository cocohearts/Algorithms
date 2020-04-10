import AVLTree
import random
import pretty_print


def value(node):
    if node:
        return node.val
    return None

def print_tree(root):
    pretty_print

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

