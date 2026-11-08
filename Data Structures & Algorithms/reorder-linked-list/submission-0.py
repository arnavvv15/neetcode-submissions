# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. Find the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        second = slow.next
        slow.next = None          # cut the list in two
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # 3. Merge the halves, alternating nodes
        first, second = head, prev
        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            second.next = nxt1
            first, second = nxt1, nxt2
        