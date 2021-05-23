# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # put the linked list into an array, to avoid a second pass
        list_of_nodes = []
        curr_node = head
        while curr_node is not None:
            list_of_nodes.append(curr_node)
            curr_node = curr_node.next

        # edge case: if n is the length of the list, we need to fix the head
        if n == len(list_of_nodes):
            head = head.next

        # all other cases can be covered with this
        else:
            prev_node = list_of_nodes[len(list_of_nodes) - (n + 1)]
            prev_node.next = prev_node.next.next

        return head