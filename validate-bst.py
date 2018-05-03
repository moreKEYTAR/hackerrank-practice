""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def checkBST(root):
    """Return Boolean for whether the tree attached to the root node is a Binary Search Tree.
    Return True if a single root node. 
    A BST is defined so that:
    - The $data$ value of every node in a node's left subtree is *less than* the data value of that node.
    - The $data$ value of every node in a node's right subtree is *greater than* the data value of that node.
    """

    
    def validate_BST(current, min_allowed, max_allowed):
        """Given a node object with .data, .left and .right, and integers
        representing the max and min data allowed, return whether the 
        binary search tree is valid with boolean True/False."""

        if min_allowed < current.data < max_allowed:  # validity check #1

            # must be checked whether a leaf or not
            
            if current.left is None and current.right is None:  # BASE CASE: LEAF

                return True  # don't want to return if is_leaf is false, so this format works

            else:  # has at least one child

                if current.left and current.right:  # both
                    if (current.left.data < current.data < current.right.data):  # validity check #2
                        left_is_valid = validate_BST(current.left, 
                                                     min_allowed=min_allowed, 
                                                     max_allowed=current.data)  # max gets reset for left
                        right_is_valid = validate_BST(current.right, 
                                                      min_allowed=current.data, # min gets reset for right 
                                                      max_allowed=max_allowed)
                        return (left_is_valid and right_is_valid)
                    else:  # validity check #2 failed
                        return False

                elif current.left:  # left only
                    if current.left.data < current.data:  # validity check #2
                        left_is_valid = validate_BST(current.left, 
                                                     min_allowed=min_allowed, 
                                                     max_allowed=current.data)  # max gets reset for left
                        return left_is_valid
                    else:  # validity check #2 failed
                        return False

                elif current.right:  # right only (could use else here)
                    if current.right.data > current.data:   # validity check #2
                        right_is_valid = validate_BST(current.right, 
                                                      min_allowed=current.data, # min gets reset for right 
                                                      max_allowed=max_allowed)
                        return right_is_valid

                    else:  # validity check #2 failed
                        return False
 
        else:  # validity check #1 failed
            return False

    
    # Run Main ####################################
    minimum = -float("inf")
    maximum = float("inf")
    return validate_BST(root, minimum, maximum)

#### NOTES #######################################################################

   # Fails BST:
   #     3
   #    /   \
   #   2     6
   #  / \   / \
   # 1   4  5  7

#### INPUT FOR MAKING THE 'FAIL' TREE ####
# 2
# 1 2 4 3 5 6 7
# No
    
######################
# FYI, Input:
# 2
# 1 2 3 4 5 6 7 
# goes like this (GOOD BST):

# ___    4
# __ 2      6
# _1   3  5   7








# def checkBST(root):
#     """Validates whether the root node is the root of a Binary Search Tree,
#     returning True or False.
#     Binary Search tree is defined as:

#     """

#     def is_leaf(node):
#         """Given a node object with.left and .right, returns True if
#         the node has no children. Otherwise returns False."""
#         return (node.left is None and node.right is None)

#     def validate_BST(current, min_allowed, max_allowed):
#         """Given a node object with .data, .left and .right, and integers
#         representing the max and min data allowed, return whether the
#         binary search tree is valid with boolean True/False."""

#         if is_leaf(current):  # base case
#             return True  # don't want to return if is_leaf is false, so this format works
            
#         else:  # not a leaf

#             left_is_valid = True  # True is default because if there is no left child, it is still valid.
#             right_is_valid = True  # True is default because if there is no right child, it is still valid.
    
#             if min_allowed < current.data < max_allowed:  # generations check as min and max are updated

#                 if current.left:  # left child exists
#                     if current.left.data < current.data:  # keep on
#                         left_is_valid = validate_BST(current.left, 
#                                                      min_allowed=min_allowed, 
#                                                      max_allowed=current.data)  # max gets reset for left
#                     else:  # child check fails for left
#                         return False
                    
#                 if current.right:  # right child exists
#                     if current.right.data > current.data:  # keep on
#                         right_is_valid = validate_BST(current.right, 
#                                                       min_allowed=current.data, # min gets reset for right 
#                                                       max_allowed=max_allowed)
#                     else:  # child check fails for right
#                         return False
           
#             else:  # failed generations check
#                 return False
            
#         return (left_is_valid and right_is_valid)
    
#     # Run Main ####################################
#     minimum = -float("inf")
#     maximum = float("inf")
#     return validate_BST(root, minimum, maximum)






# # PARENTS DO THE MULTI-GEN COMPARISON. 
# def checkBST(root):
    
#     def is_leaf(node):
#         return (node.left is None and node.right is None)

    
#     def validate_BST(current, parent):  # parent is an int value
#         """Given a node object with .data, .left and .right, and an integer
#         representing the data of the parent object, return whether the 
#         binary search tree is valid, from parent to current node to child."""
#         # ancestors goes in order of highest up in the tree to the lowest

#         if is_leaf(current):
#             return True  # don't want to return if is_leaf is false, so this format works
            
#         else: 
#             # print "starting with a non-leaf:", current.data

#             if current.left and current.right:  # two children
#                 if current.left.data < current.data < current.right.data:  # condition 1: values correct when compared to current
#                     # update our lists
#                     left_ancestors = a_lst[:]
#                     left_ancestors.append(current.left.data)
#                     right_ancestors = a_lst[:]
#                     right_ancestors.append(current.right.data)
#                     print left_ancestors
#                     print right_acestors
                    
#                     if len(left_ancestors) > 
#                         # print "checking...", current.data
#                         left_is_valid = validate_BST(current.left)
#                         # print left_is_valid, "for", current.data, "...left_is_valid value"
#                         right_is_valid = validate_BST(current.right)
#                         # print right_is_valid, "for", current.data, "...right_is_valid value"
                    
                        
#                 else:
#                     return False

#             elif current.left:  # and not current.right, because we already checked that
#                 if current.left.data < current.data:
#                     left_is_valid = validate_BST(current.left)
#                     right_is_valid = True  # Sets you up to have both variables, and right IS valid (as it is None)
#                 else:
#                     return False

#             else:  # current.right only
#                 if current.right.data > current.data:
#                     right_is_valid = validate_BST(current.right)
#                     left_is_valid = True # Sets you up to have both variables, and left IS valid (as it is None)
#                 else:
#                     return False
            
#             # we will only get here if we have not returned False already in current frame
#                 # though a validation could have come back as false
            
#             return (left_is_valid and right_is_valid)
    
#     # Run Main ####################################

#     return validate_BST(root, root.data)

# #### NOTES #######################################################################
#    #     3
#    #    /   \
#    #   2     6
#    #  / \   / \
#    # 1   4  5  7
    
# ######################
# # FYI, Input:
# # 2
# # 1 2 3 4 5 6 7 
# # goes like this.

# # ___    4
# # __ 2      6
# # _1   3  5   7
# ######################
# #             if current.left.data < current.data:
# #                 lst_of_lefts = validate_BST(current.left, previous)  
# #                 # returns those on the left in a list, if valid; otherwise return False
                
# #                 if isinstance(lst_of_lefts, list):
# #                     lst_of_lefts.sort(reverse=True)  # will have any grandchildren
                    
# #                     if lst_of_lefts[0] < current.data:  # checking all descendants
# #                         # then we are good, keep going...
# #                 else: 
# #                     return False
# #             else:
# #                 return False
        
# #         else:  # just current.right, and not current.left
# #             print "just a right one"
# #             return False
                
# #     def tracking_BST(current, lefts=None, rights=None)

# #         # lefts = lefts or []
# #         # rights = rights or []
        
# #         if current.left is None and current.right is None:
# #             return [current.data]  # nothing to append to the lists, so starts list!

# #         else:
# #             if current.left:
# #                 if current.left.data >= current.data:
# #                     return False
# #                 else:  # current.left.data < current.data:
# #                     left_is_good = tracking_BST(current.left)  # will return False or the data value or a list
# #                     if not left_is_good:  # False
# #                         return False
# #                     else: 
# #                         lefts.extend(left_is_good)  # data now in list 

# #             if current.right:
# #                 if current.right.data <= current.data:
# #                     return False
# #                 else:  # current.right.data > current.data
# #                     right_is_good = tracking_BST(current.right)
# #                     if not right_is_good:
# #                         return False
# #                     else: rights.extend(right_is_good)  # data now in list

# #         lefts.sort(reverse=True)  # Largest value is first, which should be lower than current
# #         rights.sort()  # Smallest value is first, which should be higher than the current
# #         if lefts[0] < current.data and rights[0] > current.data:
# #             return 
    
# #     tracking_BST(current)



# ########################################################################
# """ Node is defined as
# class node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
# """
# # PARENTS DO THE MULTI-GEN COMPARISON. 
# def checkBST(root):
    
#     def is_leaf(node):
#         return (node.left is None and node.right is None)

    
#     def validate_BST(current, min_allowed, max_allowed):
#         """Given a node object with .data, .left and .right, and integers
#         representing the max and min data allowed, return whether the 
#         binary search tree is valid with boolean True/False."""

#         if is_leaf(current):  # base case
#             return True  # don't want to return if is_leaf is false, so this format works
            
#         else:  # not a leaf
#             # ___    4
#             # __ 2      6
#             # _1   3  5   7

#             left_is_valid = True  # True is default because if there is no left child, it is still valid.
#             right_is_valid = True  # True is default because if there is no right child, it is still valid.
    
#             if min_allowed < current.data < max_allowed:  # generations check as min and max are updated

#                 if current.left:  # left child exists
#                     if current.left.data < current.data:  # keep on
#                         left_is_valid = validate_BST(current.left, 
#                                                      min_allowed, 
#                                                      max_allowed=current.data)  # max gets reset for left
#                     else:  # child check fails for left
#                         return False
                    
#                 if current.right:  # right child exists
#                     if current.right.data > current.data:  # keep on
#                         right_is_valid = validate_BST(current.right, 
#                                                       min_allowed=current.data, # min gets reset for right 
#                                                       max_allowed)
#                     else:  # child check fails for right
#                         return False
# #                 if (current.left.data < current.data < current.right.data and   # condition 1
# #                     current.data < max_allowed and  # condition 2
# #                     current.data > min_allowed):  # condition 3


# #                     left_is_valid = validate_BST(current.left, 
# #                                                  min_allowed, max_allowed=current.data) # max gets reset for left
# #                     right_is_valid = validate_BST(current.right, 
# #                                                   min_allowed=current.data, max_allowed)              
#             else:  # failed generations check
#                 return False

# #             elif current.left:  # and not current.right, because we already checked that
# #                 if (current.left.data < current.data and
# #                     current.data < max_allowed and
# #                     current.data > min_allowed):

# #                     left_is_valid = validate_BST(current.left)
# #                     right_is_valid = True  # Sets you up to have both variables, and right IS valid (as it is None)
# #                 else:
# #                     return False

# #             else:  # current.right only
# #                 if current.right.data > current.data:
# #                     right_is_valid = validate_BST(current.right)
# #                     left_is_valid = True # Sets you up to have both variables, and left IS valid (as it is None)
# #                 else:
# #                     return False
            
#             # we will only get here if we have not returned False already in current frame
#                 # though a validation could have come back as false
            
#             return (left_is_valid and right_is_valid)
    
#     # Run Main ####################################
#     minimum = -(float(inf))
#     maximum = float(inf)
#     return validate_BST(root, minimum, maximum)

# #### NOTES #######################################################################
#    #     3
#    #    /   \
#    #   2     6
#    #  / \   / \
#    # 1   4  5  7
    
# ######################
# # FYI, Input:
# # 2
# # 1 2 3 4 5 6 7 
# # goes like this.

# # ___    4
# # __ 2      6
# # _1   3  5   7


# #            8
#       5             14
    
#    3     6       12      16

#  1     4  7     9  13   15  18



######################
#             if current.left.data < current.data:
#                 lst_of_lefts = validate_BST(current.left, previous)  
#                 # returns those on the left in a list, if valid; otherwise return False
                
#                 if isinstance(lst_of_lefts, list):
#                     lst_of_lefts.sort(reverse=True)  # will have any grandchildren
                    
#                     if lst_of_lefts[0] < current.data:  # checking all descendants
#                         # then we are good, keep going...
#                 else: 
#                     return False
#             else:
#                 return False
        
#         else:  # just current.right, and not current.left
#             print "just a right one"
#             return False
                
#     def tracking_BST(current, lefts=None, rights=None)

#         # lefts = lefts or []
#         # rights = rights or []
        
#         if current.left is None and current.right is None:
#             return [current.data]  # nothing to append to the lists, so starts list!

#         else:
#             if current.left:
#                 if current.left.data >= current.data:
#                     return False
#                 else:  # current.left.data < current.data:
#                     left_is_good = tracking_BST(current.left)  # will return False or the data value or a list
#                     if not left_is_good:  # False
#                         return False
#                     else: 
#                         lefts.extend(left_is_good)  # data now in list 

#             if current.right:
#                 if current.right.data <= current.data:
#                     return False
#                 else:  # current.right.data > current.data
#                     right_is_good = tracking_BST(current.right)
#                     if not right_is_good:
#                         return False
#                     else: rights.extend(right_is_good)  # data now in list

#         lefts.sort(reverse=True)  # Largest value is first, which should be lower than current
#         rights.sort()  # Smallest value is first, which should be higher than the current
#         if lefts[0] < current.data and rights[0] > current.data:
#             return 
    
#     tracking_BST(current)


    


    