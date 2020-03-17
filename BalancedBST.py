import time
import random

class Node:

    def __init__(self,key,parent = None,height = 0):
        self.parent = parent
        self.left = None
        self.right = None
        self.key = key
        self.height = 0

    @staticmethod
    def height(node):
        if node == None:
            return -1
        return node.height

    def sibling(self,node):
        if node.parent == None:
            return None
        if node.parent.left == node:
            return node.parent.right
        if node.parent.right == node:
            return node.parent.left

    # adjusts heights from one node upwards
    def recalculate_heights(self):
        if self.height != 1 + max(Node.height(self.left),Node.height(self.right)):
            self.height = 1 + max(Node.height(self.left),Node.height(self.right))
            if self.parent != None:
                self.parent.recalculate_heights()
        return

    # inserts node into tree with root "root"
    def insert_without_rotation(self,root):
        # then node is on the right side of root
        if root.key < self.key:
            if root.right == None:
                self.parent = root
                root.right = self
            else:
                Node.insert_without_rotation(self, root.right)
        elif root.key >= self.key:
            if root.left == None:
                self.parent = root
                root.left = self
            else:
                Node.insert_without_rotation(self, root.left)

    # returns the highest node in the tree
    @staticmethod
    def rootify(root):
        node_parent = root
        while not node_parent.parent == None:
            node_parent = node_parent.parent
        return node_parent

    # assumes node has a right child
    def left_rotate(self, node):
        # put node.right in its place
        node.right.parent = node.parent
         # if node is a left child:
        if not(node.parent == None):
            if node.parent.left == node:
                node.parent.left = node.right
            # if node is a right child:
            else:
                node.parent.right = node.right
        node.parent = node.right
        # put node.right.left in its place
        node.right = node.parent.left
        # put node in its place
        node.parent.left = node
        if not node.right == None:
            node.right.parent = node
        # heights:
        Node.recalculate_heights(node)

    # assumes node has a left child
    def right_rotate(node):
        #put node.left in its place
        node.left.parent = node.parent
        # if node is a right child:
        if not(node.parent == None):
            if node.parent.right == node:
                node.parent.right = node.left
            # if node is a left child:
            else:
                node.parent.left = node.left
        node.parent = node.left
        # put node.left.right in its place
        node.left = node.parent.right
        # put node in its place
        node.parent.right = node
        if not node.left == None:
            node.left.parent = node
        # heights:
        Node.recalculate_heights(node)



    def rotatation_adjusting_heights(node):
        """

        """
        counter_node = node
        while not(counter_node == None):
            height_differences = Node.height(counter_node.right) - Node.height(counter_node.left)
            # actual rotation
            # if counter_node violates AVL on the left side:
            if height_differences < -1:
                # if counter_node.left is right-heavy:
                if Node.height(counter_node.left.right) > Node.height(counter_node.left.left):
                    Node.left_rotate(counter_node.left)
                    Node.right_rotate(counter_node)

                    Node.recalculate_heights(counter_node)
                # else, counter_node.left is balanced or left-heavy
                else:
                    Node.right_rotate(counter_node)

                    Node.recalculate_heights(counter_node)


            # elif counter_node violated AVL on the right side:
            elif height_differences > 1:
                # if counter_node.right is left-heavy:
                if Node.height(counter_node.right.left) > Node.height(counter_node.right.right):
                    Node.right_rotate(counter_node.right)
                    Node.left_rotate(counter_node)

                    Node.recalculate_heights(counter_node)
                # else, counter_node.right is either balanced or right-heavy
                else:
                    Node.left_rotate(counter_node)

                    Node.recalculate_heights(counter_node)
            # end of actual rotation

            counter_node = counter_node.parent

    def insert(root,key):
        """
        Inserts a key into tree rooted at root
        """
        node = Node(key)
        node.insert_without_rotation(root)
        Node.recalculate_heights(node)
        Node.rotatation_adjusting_heights(node)
    
    def delete(node):
        """
        Deletes a node from the tree its a part of
        """
        #first we find a good candidate for a key switch
        if node.right != None:
            candidate = node.right
            while candidate.left != None:
                candidate = candidate.left
        #if not that then the node doesnt have a right child, so just swap with left child
        else:
            candidate = node.left
        #either way, candidate is a left child
        node.key = candidate.key
        candidate.parent.left = None
        Node.recalculate_heights(candidate.parent)
        Node.rotatation_adjusting_heights(candidate.parent)
        del candidate


    def LCA(node1,node2,root):
        """
        node1.key < node2.key. Obviously root doesnt have to be the actual root; node1 and node2 have to be in subtree rooted at root
        """
        counter_node = root
        l = node1.key
        h = node2.key
        while (not counter_node.key >= l) or (not counter_node.key <= h):
            if counter_node.key < l:
                counter_node = counter_node.right
            else:
                counter_node = counter_node.left
        return counter_node

    def NodeList(node,l,h,result):
        if node == None:
            return
        if node.key >= l and node.key <= h:
            result.append(node)
        if node.key >= l:
            Node.NodeList(node.left,l,h,result)
        if node.key <= h:
            Node.NodeList(node.right,l,h,result)
        
    def List_Range_Query(node1,node2,root):
        Least_CA = Node.LCA(node1,node2,root)
        list1 = []
        Node.NodeList(Least_CA,node1.key,node2.key,list1)
        return list1

class BalancedBST:
    """
    A class, one instance of which is an entire tree.
    """
    def __init__(self,firstkey = None):
        if firstkey != None:
            ournode = Node(firstkey)
            self.root = ournode
        else:
            self.root = None

    def insert(self,key):
        if self.root == None:
            self.root = Node(key)
        else:
            Node.insert(self.root,key)
            self.root = Node.rootify(self.root)

    def delete(self,key):
        #first we find the node with key key
        node = self.root
        while node.key != key:
            if node.key > key:
                node = node.left
            else:
                node = node.right
        Node.delete(node)


    def inclusive_range_query(self,beginning,end):
        # first we find node1, the node with smallest key at least beginning
        node1 = self.root
        if node1.key < beginning and not node1.right == None:
            node1 = node1.right
        if node1.key > beginning and not node1.left == None:
            if node1.left >= beginning:
                node1 = node1.left
        
        # similarly find node2
        node2 = self.root
        if node2.key > end and not node2.left == None:
            node2 = node2.left
        if node2.key < end and not node2.right == None:
            if node2.right <= end:
                node2 = node2.left
        
        return Node.List_Range_Query(node1,node2,self.root)