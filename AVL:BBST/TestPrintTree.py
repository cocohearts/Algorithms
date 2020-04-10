import print_tree
import pretty_print
import random
import AVLTree

tree = AVLTree.AVL_Tree()
length = 40
my_list = list(range(10000000,10000000+length))
random.shuffle(my_list)
root = None
for key in my_list:
    root = tree.insert(root,key)
pretty_print.BinaryTree.pretty_print(root)
print("\n")
print_tree.PrintTree.print_tree(root)

