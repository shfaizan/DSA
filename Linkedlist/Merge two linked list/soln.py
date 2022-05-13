# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        return dummy.next


def append(head, val):
    while head.next:
        head = head.next
    head.next = ListNode(val)


def print_list(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    head1 = ListNode(1)
    append(head1, 2)
    append(head1, 4)
    head2 = ListNode(1)
    append(head2, 3)
    append(head2, 4)
    print_list(Solution().mergeTwoLists(head1, head2))


