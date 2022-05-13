from typing import Optional
from linked_list import start_append_single_head, print_ll


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next



if __name__ == '__main__':
    head = start_append_single_head([1, 2])
    n = 2
    print_ll(Solution().removeNthFromEnd(head, n))
