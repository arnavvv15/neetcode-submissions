# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # Move fast n + 1 steps
        for i in range(n + 1):
            fast = fast.next

        # Move both pointers
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove nth node
        slow.next = slow.next.next

        return dummy.next
        