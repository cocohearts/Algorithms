# Python code to insert a node in AVL tree 
  
# Generic tree node class
class TreeNode(): 
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None
        self.height = 0
  
# AVL tree class which supports the
# Insert operation 
class AVL_Tree():
    """
    Recursive function to insert key in  subtree rooted with node and returns 
    new root of subtree. 
    """
    def insert(self, root, key):
        """
        Will return new root and do all recursive balancing/insertion.
        """
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(AVL_Tree.getHeight(root.left),
                           AVL_Tree.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        placeholder1 = y.left

        # Perform rotation
        y.left = z
        z.right = placeholder1

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
  
        # Return the new root 
        return y 

    def rightRotate(self, z):

        y = z.left
        placeholder2 = y.right

        # Perform rotation
        y.right = z
        z.left = placeholder2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right)) 
  
        # Return the new root
        return y

    @staticmethod
    def getHeight(root):
        """
        Generalizes root.height to root == None => -1
        """
        if not root:
            return -1

        return root.height

    def getBalance(self, root):
        """
        If None, return -1, else return root.left.height - root.right.height
        """
        if not root:
            return -1

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.val))
        self.preOrder(root.left)
        self.preOrder(root.right)
    
    def find_node(self,root,key):
        """
        Finds the node in self with value key
        """
        node = root
        while node.val != key:
            if node.val < key:
                node = node.right
            else:
                node = node.left
        return node
    
    def delete(self,root,key):
        """
        Deletes key from self, returns None
        """
        return self.recursive_delete(root,key,"key")


    def recursive_delete(self,root,key,mode):
        """
        Algorithm:
        Initially mode is unmutable string "key".
        We recurse starting from root.
        Once we hit node st node.val = key then somehow save that node as global
        "special node", then mode changed to "node"
        After that recursion changes from based on recursed.val to just left
        Once hit bottom (candidate) then copy candidate.val to new_key
        change value to "special" to make it look better, do key replacement adn forgetting
        then we're out of the recursing if statements, follows height adjustment
        like in insert all the way to root
        """
        # Recursing section:
        if mode == "key":
            if root.val == key:
                global special_node
                special_node = root
                if root.right:
                    if root.right.left:
                        root.right = self.recursive_delete(root.right,key,"node")
                    else:
                        global candidate_key
                        candidate_key = root.right.val

                        root.val = root.right.val
                        root.right = None


                elif root.left:
                    # special_node has only a left child, not a right
                    global candidate_key
                    candidate_key = root.left.val

                    special_node.val = root.left.val
                    root.left = None

            elif root.val < key:
                if root.right.left or root.right.right:
                    root.right = self.recursive_delete(root.right,key,mode)
                else:
                    #root.right is a leaf
                    root.val = root.right.val
                    root.right = None

            else:
                if root.left.left or root.left.right:
                    root.left = self.recursive_delete(root.left,key,mode)
                else:
                    #root.left is a leaf
                    root.val = root.left.val
                    root.left = None

        elif mode == "node":
            if root.left:
                if root.left.left:
                    root.left = self.recursive_delete(root.left,key,mode)
                else:
                    global candidate_key
                    candidate_key = root.left.val
                    special_node.val = candidate_key
                    root.left = None

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and candidate_key > root.left.val:
            return self.rightRotate(root)

        # Case 2 - Right Right
        if balance < -1 and candidate_key < root.right.val:
            return self.leftRotate(root)

        # Case 3 - Left Right
        if balance > 1 and candidate_key < root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        if balance < -1 and candidate_key > root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    @staticmethod
    def LCA(root,node1,node2):
        """
        node1.key < node2.key. Obviously root doesnt have to be the actual root; node1 and node2 have to be in subtree rooted at root
        """
        counter_node = root
        l = node1.val
        h = node2.val
        while (not counter_node.val >= l) or (not counter_node.val <= h):
            if counter_node.val < l:
                counter_node = counter_node.right
            else:
                counter_node = counter_node.left
        return counter_node