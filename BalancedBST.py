class Node:

    def __init__(self,key,parent = None,height = 0):
        self.parent = parent
        self.left = None
        self.right = None
        self.key = key
        self.height = 0

    def sibling(node):
        if node.parent == None:
            return None
        if node.parent.left == node:
            return node.parent.right
        if node.parent.right == node:
            return node.parent.left

    def height(node):
        if node == None:
            return -1
        else:
            return node.height
    
    # adjusts heights from one node upwards
    def recalculate_heights(node):
        if node == None:
            return None
        node.height = 1 + max(Node.height(node.left),Node.height(node.right))
    
        counter_node = node.parent
        Node.recalculate_heights(counter_node)

    # inserts node into tree with root "root"
    def insert_without_rotation(root,node):
        # then node is on the right side of root
        if root.key < node.key:
            if root.right == None:
                node.parent = root
                root.right = node
            else:
                Node.insert_without_rotation(root.right,node)
        elif root.key >= node.key:
            if root.left == None:
                node.parent = root
                root.left = node
            else:
                Node.insert_without_rotation(root.left,node)

    # returns the highest node in the tree
    def rootify(root):
        node_parent = root
        while not node_parent.parent == None:
            node_parent = node_parent.parent
        return node_parent

    # assumes node has a right child
    def left_rotate(node):
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

    def did_it_work(root_in):
        if root_in == None:
            return True
        first_test = (abs(height(root_in.left) - height(root_in.right)) <= 1)
        second_test = (max(height(root_in.left),height(root_in.right)) + 1 == root_in.height)
        if not root_in.left == None:
            third_test = (root_in.left.key <= root_in.key)
            fourth_test = root_in.left.parent == root_in
        else:
            third_test = True
            fourth_test = True

        if not root_in.right == None:
            fifth_test = (root_in.key <= root_in.right.key)
            sixth_test = root_in.right.parent == root_in
        else:
            fifth_test = True
            sixth_test = True
        seventh_test = Node.did_it_work(root_in.left)
        eighth_test = Node.did_it_work(root_in.right)

        ninth_test = (height(root_in) >= 0)

        return first_test and second_test and third_test and fourth_test and fifth_test and sixth_test and seventh_test and eighth_test and ninth_test

    def rotatation_adjusting_heights(node):
        counter_node = node
        while not(counter_node == None):
            height_differences = height(counter_node.right) - height(counter_node.left)
            # actual rotation
            # if counter_node violates AVL on the left side:
            if height_differences < -1:
                # if counter_node.left is right-heavy:
                if height(counter_node.left.right) > height(counter_node.left.left):
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
        node = Node(key)
        Node.insert_without_rotation(root,node)
        Node.recalculate_heights(node)
        Node.rotatation_adjusting_heights(node)
    
    def delete(node):
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
        recalculate_heights(candidate.parent)
        del candidate


class BalancedBST:
    def __init__(self,firstkey = None):
        if firstkey != None:
            ournode = Node(firstkey)
            self.root = ournode
        else:
            self.root = None

    def insert(key):
        if self.root == None:
            self = Node(key)
        else:
            Node.insert(self.root,key)
            root = rootify(root)

    def delete(node):
        Node.delete(node)
