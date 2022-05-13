from typing import Optional
from linked_list import start_append_single_head, print_ll


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp

        count = 1
        tmp = ListNode()
        tmp.next = prev
        final = tmp
        curr = tmp.next
        while curr:
            if count == n:
                tmp.next = curr.next
                break
            else:
                tmp = tmp.next
                curr = tmp.next
                count += 1
        pre1 = None
        curr = final.next
        while curr:
            tmp = curr.next
            curr.next = pre1
            pre1 = curr
            curr = tmp
        return pre1


if __name__ == '__main__':
    head = start_append_single_head([1, 2])
    n = 2
    print_ll(Solution().removeNthFromEnd(head, n))
