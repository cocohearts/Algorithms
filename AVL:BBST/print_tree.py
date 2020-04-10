import AVLTree
import math

class PrintTree:
    @staticmethod
    def print_tree(root):
        width_tracker = {}
        PrintTree.node_widths(root,width_tracker)

        current_list_nodes = [root]
        list_children_nodes = []
        
        num_str = ""
        symb_str = ""

        ld = u"\u250f"
        rd = u"\u2513"
        up = u"\u253b"
        lu = u"\u251b"
        ru = u"\u2517"
        dash = u"\u2501"
        space = " "
        padding = " "

        #while PrintTree.my_bool(current_list_nodes) or PrintTree.my_bool(list_children_nodes):
            
        #    if current_list_nodes:

        while True:

            if not (PrintTree.my_bool(current_list_nodes) or PrintTree.my_bool(list_children_nodes)):
                print(num_str)
                break
            
            if current_list_nodes:
                node = current_list_nodes.pop(0)

                if type(node) == int:
                    num_str += padding * node
                    symb_str += padding * node
                    list_children_nodes.append(node)
                    continue

                node_left = (width_tracker[node] - len(str(node.val))) // 2
                node_right = (width_tracker[node] - len(str(node.val)))- (width_tracker[node] - len(str(node.val))) // 2
                num_str += space * node_left
                num_str += str(node.val)
                num_str += space * node_right

                if node.left and node.right:
                    node_left_left = (width_tracker[node.left] - len(str(node.left.val))) // 2
                    node_right_right = (width_tracker[node.right] - len(str(node.right.val)))- (width_tracker[node.right] - len(str(node.right.val))) // 2

                    symb_str += space * node_left_left
                    symb_str += ld
                    symb_str += dash * (node_left - node_left_left - 1)
                    symb_str += up
                    symb_str += dash * ((len(str(node.val)) - 1) + (node_right - node_right_right - 1))
                    symb_str += rd
                    symb_str += space * node_right_right

                    list_children_nodes += [node.left,len(str(node.val)),node.right]
                
                elif node.left:
                    node_left_left = (width_tracker[node.left] - len(str(node.left.val))) // 2

                    symb_str += space * node_left_left
                    symb_str += ld
                    symb_str += dash * (node_left - node_left_left - 1)
                    symb_str += lu
                    symb_str += space * (node_right + len(str(node.val))-1)

                    list_children_nodes += [node.left,len(str(node.val))+1]
                
                elif node.right:
                    node_right_right = (width_tracker[node.right] - len(str(node.right.val))) // 2

                    symb_str += space * (node_left + len(str(node.val))-1)
                    symb_str += ru
                    symb_str += dash * (node_right - node_right_right - 1)
                    symb_str += rd
                    symb_str += space * node_right_right
                
                    list_children_nodes += [len(str(node.val))+1,node.right]

                else:
                    symb_str += space * width_tracker[node]
                
                    list_children_nodes += [len(str(node.val))+2]

            else:
                print(num_str)
                print(symb_str)
                current_list_nodes = list_children_nodes
                list_children_nodes = []
                num_str = ""
                symb_str = ""

    @staticmethod
    def node_widths(root,tracker):
        if root == None:
            return 1
        tracker[root] = PrintTree.node_widths(root.left,tracker) + PrintTree.node_widths(root.right,tracker) + len(str(root.val))
        return tracker[root]
    
    @staticmethod
    def my_bool(my_list):
        for item in my_list:
            if type(item) != int:
                return True
        return False