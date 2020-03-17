import numpy as np
import time
import random
import BalancedBST

class BalancedBSTTest:
    """
    Each instance is a BalancedBST instance with insertion order a permutation of range(2000).
    """
    def __init__(self):
        self.tree = BalancedBST.BalancedBST()
        my_list = np.random.permutation(range(2000))
        for key in my_list:
            BalancedBST.BalancedBST.insert(self.tree,key)
        
    def did_it_work(self):
        return self.recursive_did_it_work(self.tree.root)

    def recursive_did_it_work(self,node):
        first_test = (abs(BalancedBST.Node.height(node.left) - BalancedBST.Node.height(node.right)) <= 1)
        second_test = (max(BalancedBST.Node.height(node.left),BalancedBST.Node.height(node.right)) + 1 == node.height)
        if not node.left == None:
            third_test = (node.left.key <= node.key)
            fourth_test = node.left.parent == node
            seventh_test = self.recursive_did_it_work(node.left)
        else:
            third_test = True
            fourth_test = True
            seventh_test = True

        if not node.right == None:
            fifth_test = (node.key <= node.right.key)
            sixth_test = node.right.parent == node
            eighth_test = self.recursive_did_it_work(node.right)
        else:
            fifth_test = True
            sixth_test = True
            eighth_test = True

        ninth_test = (BalancedBST.Node.height(node) >= 0)

        return first_test and second_test and third_test and fourth_test and fifth_test and sixth_test and seventh_test and eighth_test and ninth_test
if __name__ == "__main__":
    my_test = BalancedBSTTest()
    print(my_test.did_it_work())