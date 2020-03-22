import unittest
#import numpy as np
import time
import random

import AVLTree

class TestAVLTree(unittest.TestCase):

    def recursive_iteration(self, root, validator):
        """
        Executes self.validator() on all nodes in tree rooted at root
        """
        if(root == None):
            return
        validator(root)
        self.recursive_iteration(root.left, validator)
        self.recursive_iteration(root.right, validator)
        
    def init_avl_tree(self):
        """
        Creates an AVL tree with indices in range(constant), and insertion order is random
        """
        tree = AVLTree.AVL_Tree()
        length = 1000
        my_list = list(range(length))
        random.shuffle(my_list)
        root = None
        for key in my_list:
            root = tree.insert(root,key)
        return root
    
    def init_del_avl_tree(self):
        tree2 = AVLTree.AVL_Tree()
        my_list = list(range(1000))
        extract = random.sample(my_list,500)
        root = None
        for key in my_list:
            root = tree2.insert(root,key)
        for key in my_list:
            if key not in extract:
                root = tree2.delete(root,key)
        return [root,extract]


    def print_tree(self, root):
        print(root.val, root.left.val if root.left else None, root.right.val if root.right else None)
        if root.left:
            self.print_tree(root.left)
        if root.right:
            self.print_tree(root.right)

    def height_diff_leq_one(self, node):
        self.assertTrue(abs(AVLTree.AVL_Tree.getHeight(node.left) - AVLTree.AVL_Tree.getHeight(node.right)) <= 1)

    def parent_height_sum(self, node):
        self.assertEqual(max(AVLTree.AVL_Tree.getHeight(node.left),AVLTree.AVL_Tree.getHeight(node.right)) + 1, node.height)
    
    def left_keys_less_key(self,node):
        if not node.left:
            return
        self.assertTrue(node.val > node.left.val)
        self.assertTrue(self.largest_key_left_subtree(node) < node.val)

    def largest_key_left_subtree(self,node):
        if node.right == None:
            return float("-inf")
        counter_node = node.left
        while counter_node.right:
            counter_node = counter_node.right
        return counter_node.val
    
    def right_keys_greater_key(self,node):
        if not node.right:
            return
        self.assertTrue(node.val < node.right.val)
        self.assertTrue(self.smallest_key_right_subtree(node) > node.val)
    
    def smallest_key_right_subtree(self,node):
        if node.right == None:
            return float("inf")
        counter_node = node.right
        while counter_node.left:
            counter_node = counter_node.left
        return counter_node.val
    
    def height_geq_0(self,node):
        return node.val >= 0
    
    def set_keys(self,root):
        my_set = set([])
        return self.recursive_members(root,my_set)

    def recursive_members(self,root,my_set):
        if root:
            my_set.add(root)
            my_set.update(self.recursive_members(root.left,my_set))
            my_set.update(self.recursive_members(root.right,my_set))
        return my_set

    def test_height_diff_leq_one(self):
        root = self.init_avl_tree()
#        self.recursive_iteration(root, self.print_node)
        self.recursive_iteration(root, self.height_diff_leq_one)
    
    def test_parent_height_sum(self):
        root = self.init_avl_tree()
        self.recursive_iteration(root, self.parent_height_sum)
    
    def test_left_keys_less_key(self):
        root = self.init_avl_tree()
        self.recursive_iteration(root, self.left_keys_less_key)
    
    def test_right_keys_greater_key(self):
        root = self.init_avl_tree()
        self.recursive_iteration(root,self.right_keys_greater_key)

    def test_height_geq_0(self):
        root = self.init_avl_tree()
        self.recursive_iteration(root,self.height_geq_0)
    
    def test_delete(self):
        my_list = self.init_del_avl_tree()
        self.assertTrue(set(my_list[1]),self.set_keys(my_list[0]))
    
    def test_del_height_diff_leq_one(self):
        root = self.init_del_avl_tree()[0]
        self.recursive_iteration(root, self.height_diff_leq_one)
    
    def test_del_parent_height_sum(self):
        root = self.init_del_avl_tree()[0]
        self.recursive_iteration(root, self.parent_height_sum)
    
    def test_del_left_keys_less_key(self):
        root = self.init_del_avl_tree()[0]
        self.recursive_iteration(root, self.left_keys_less_key)
    
    def test_del_right_keys_greater_key(self):
        root = self.init_del_avl_tree()[0]
        self.recursive_iteration(root,self.right_keys_greater_key)

    def test_del_height_geq_0(self):
        root = self.init_del_avl_tree()[0]
        self.recursive_iteration(root,self.height_geq_0)

if __name__ == '__main__':
    unittest.main()