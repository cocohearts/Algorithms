import unittest
#import numpy as np
import time
import random
import BalancedBST

class TestBBST(unittest.TestCase):

    def recursive_iteration(self, root, validator):
        if(root == None):
            return
        validator(root)
        self.recursive_iteration(root.left, validator)
        self.recursive_iteration(root.right, validator)
        
    def init_bbst(self):
        self.tree = BalancedBST.BalancedBST()
#       my_list = np.random.permutation(range(10))
        my_list = list(range(10))
        random.shuffle(my_list)
        print(my_list)
        for key in my_list:
            BalancedBST.BalancedBST.insert(self.tree,key)

    def compare_height_diff(self, node):
        self.assertTrue(abs(BalancedBST.Node.height(node.left) - BalancedBST.Node.height(node.right)) <= 1)
#        print(BalancedBST.Node.height(node.left))

    def parent_height_sum(self, node):
        if((max(BalancedBST.Node.height(node.left),BalancedBST.Node.height(node.right)) + 1 == node.height) == False):
            print("this is the error node")
            self.print_node(node)
        self.assertTrue(max(BalancedBST.Node.height(node.left),BalancedBST.Node.height(node.right)) + 1 == node.height)
        
    def print_node(self, node):
        print(node.key, node.left.key if node.left != None else None, node.right.key if node.right!= None else None)
    
    def test_height_diff_leq_one(self):
        self.init_bbst()
        self.recursive_iteration(self.tree.root, self.print_node)
        self.recursive_iteration(self.tree.root, self.compare_height_diff)
    
    def test_parent_height_sum(self):
        self.init_bbst()
        self.recursive_iteration(self.tree.root, self.print_node)
        self.recursive_iteration(self.tree.root, self.parent_height_sum)

if __name__ == '__main__':
    unittest.main()