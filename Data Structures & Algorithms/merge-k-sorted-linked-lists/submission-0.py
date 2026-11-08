# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 1. Collect every value
        values = []
        for node in lists:
            while node:
                values.append(node.val)
                node = node.next
        values.sort()
        dummy = tail = ListNode()
        for v in values:
            tail.next = ListNode(v)
            tail = tail.next
        return dummy.next
        