from typing import Optional
from linked_list import start_append_single_head, print_ll, rand_head

"""
# Definition for a ListNode1.
"""


class ListNode1:
    def __init__(self, x: int, next: 'ListNode1' = None, random: 'ListNode1' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[ListNode1]') -> 'Optional[ListNode1]':
        oldToCopy = {None: None}
        curr = head
        while curr:
            copy = ListNode1(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]


if __name__ == '__main__':
    head = Solution().copyRandomList(rand_head)
    print_ll(head)
