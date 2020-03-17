import unittest
#import numpy as np
import time
import random
import AVLTree

class TestAVLTree(unittest.TestCase):

    def recursive_iteration(self, root, validator):
        if(root == None):
            return
        validator(root)
        self.recursive_iteration(root.left, validator)
        self.recursive_iteration(root.right, validator)
        
    def init_avl_tree(self):
        tree = AVLTree.AVL_Tree()
#       my_list = np.random.permutation(range(10))
        my_list = list(range(1000))
        random.shuffle(my_list)
#        print(my_list)
        root = None
        for key in my_list:
            root = tree.insert(root,key)
        return root

    def compare_height_diff(self, node):
        self.assertTrue(abs(AVLTree.AVL_Tree.getHeight(node.left) - AVLTree.AVL_Tree.getHeight(node.right)) <= 1)

    def parent_height_sum(self, node):
        self.assertEqual(max(AVLTree.AVL_Tree.getHeight(node.left),AVLTree.AVL_Tree.getHeight(node.right)) + 1, node.height)
        
    def print_node(self, node):
        print(node.val, node.left.val if node.left else None, node.right.val if node.right else None)
    
    def test_height_diff_leq_one(self):
        root = self.init_avl_tree()
#        self.recursive_iteration(root, self.print_node)
        self.recursive_iteration(root, self.compare_height_diff)
    
    def test_parent_height_sum(self):
        root = self.init_avl_tree()
#        self.recursive_iteration(root, self.print_node)
        self.recursive_iteration(root, self.parent_height_sum)

if __name__ == '__main__':
    unittest.main()