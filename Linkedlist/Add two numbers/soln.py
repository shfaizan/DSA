from typing import Optional
from linked_list import start_append_single_head, print_ll


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry
            carry = sum // 10
            val = sum % 10
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 7]
    l1 = start_append_single_head(l1)
    l2 = start_append_single_head(l2)
    print_ll(Solution().addTwoNumbers(l1, l2))
