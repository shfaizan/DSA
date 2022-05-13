from typing import Optional
from linked_list import start_append_single_head, print_ll


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        hashmap = {}
        while head:
            if head in hashmap:
                return True
            hashmap[head] = head
            head = head.next
        return False



if __name__ == "__main__":
    head = start_append_single_head([3, 2, 0, -4])
    pos = 1
    print(Solution().hasCycle(head))

