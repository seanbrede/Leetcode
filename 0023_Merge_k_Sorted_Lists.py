# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []

        # put every node from each list into the heap
        for node in lists:
            while node is not None:
                heapq.heappush(heap, -node.val)
                node = node.next

        # pull every node out of the heap
        head = None
        while heap:
            new = ListNode(val=(heappop(heap) * -1), next=head)
            head = new

        return head
