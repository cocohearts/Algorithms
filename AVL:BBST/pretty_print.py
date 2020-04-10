import math
import os

class TreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.pp_width = 0



class BinaryTree:

    @staticmethod
    def pretty_print(root):
        ld = u"\u250f"
        rd = u"\u2513"
        up = u"\u253b"
        lu = u"\u251b"
        ru = u"\u2517"
        dash = u"\u2501"
        space = "-"
        padding = "*"
        
        line_breaker_node = TreeNode(math.pi)
        BinaryTree.__calculate_pp_width(root)

        rows, columns = os.popen('stty size', 'r').read().split()
        if (root.pp_width > columns):
            print(
                    "The terminal width is less than the tree width. Can't do pretty print."
            )
            return
        
        tracking_queue = [line_breaker_node]
        node_row = ""
        line_row = ""
        node = root
        terminate = False

        while len(tracking_queue) > 0:
            if (node == line_breaker_node):    #new_line_node
                if terminate:
                    return
                tracking_queue.append(line_breaker_node)
                print(node_row)
                print(line_row)
                node_row = ""
                line_row = ""
                terminate = True

            elif (node.val == -math.pi):    # padding node
                BinaryTree.__add_padding_node(tracking_queue, node.pp_width)
                node_row += padding * node.pp_width
                line_row += padding * node.pp_width

            else:    # print curent node and the line (arrows to the children)
                terminate = False
                # construct the node block for the current row
                current_node_block = list(space * node.pp_width)
                val_offset = (node.pp_width - len(str(node.val))) // 2
                # add node value
                BinaryTree.__add_str_in_place(current_node_block, val_offset,
                                                                            str(node.val))
                node_row += "".join(current_node_block)

                # construct the line block for the current row
                current_line_block = list(space * node.pp_width)
                if (node.left is not None and node.right is not None):
                    current_line_block[val_offset] = up    
                elif (node.left is None and node.right is not None):
                    current_line_block[val_offset] = ru    
                elif (node.left is not None and node.right is None):
                    current_line_block[val_offset] = lu    

                left_node_width = 1

                if (node.left is not None):
                    tracking_queue.append(node.left)
                    left_node_width = node.left.pp_width
                    left_down_offset = (node.left.pp_width - len(str(node.left.val))) // 2
                    current_line_block[left_down_offset] = ld    
                    BinaryTree.__add_str_in_place(
                            current_line_block, left_down_offset + 1,
                            BinaryTree.__create_string(dash,    val_offset - left_down_offset - 1))
                else:
                    BinaryTree.__add_padding_node(tracking_queue, 1)

                # need to add padding node to the queue so that next level print can be alighed properly
                BinaryTree.__add_padding_node(tracking_queue, len(str(node.val)))

                if (node.right is not None):
                    tracking_queue.append(node.right)
                    right_down_offset = left_node_width \
                                             + len(str(node.val)) \
                                             + (node.right.pp_width + len(str(node.right.val)))//2 \
                                             - 1
                    current_line_block[right_down_offset] = rd    
                    BinaryTree.__add_str_in_place(
                            current_line_block, val_offset + 1,
                            BinaryTree.__create_string(dash,    right_down_offset - val_offset - 1))    
                else:
                    BinaryTree.__add_padding_node(tracking_queue, 1)
                #end if
                line_row += "".join(current_line_block)
            #end else
            node = tracking_queue.pop(0)
        #end while

    @staticmethod
    def __create_string(ch, repeat):
        string = ''
        for i in range(repeat):
            string += ch
        return string

    @staticmethod
    def __add_str_in_place(list, offset, string):
        string_list = []
        string_list[:0] = string
        for i in range(len(string)):
            list[offset + i] = string_list[i]

    @staticmethod
    def __add_padding_node(queue, length):
        padding_node = TreeNode(-math.pi)
        padding_node.pp_width = length
        queue.append(padding_node)

    @staticmethod
    def __calculate_pp_width(root):
        if (root is None):
            return 1
        root.pp_width = BinaryTree.__calculate_pp_width(root.left) \
            + BinaryTree.__calculate_pp_width(root.right) \
            + len(str(root.val))
#        print(root.val, root.pp_width)
        return root.pp_width


def create_simple_tree():
    root = TreeNode(1546540)
    a = TreeNode(20)
    b = TreeNode(3)
    c = TreeNode(4000000)
    d = TreeNode(50)
    e = TreeNode(6056465)
    f = TreeNode(70)
    g = TreeNode(800000)
    root.left = a
    root.right = b
    a.left = c
    c.right = d
    b.left = e
    b.right = f
    f.right = g
    return root


def main():
    root = create_simple_tree()
    BinaryTree.pretty_print(root)


if __name__ == "__main__":
    main()

