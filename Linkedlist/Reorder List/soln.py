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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


def append(head, val):
    while head.next:
        head = head.next
    head.next = ListNode(val)


def print_list(head):
    while head:
        print(head.val)
        head = head.next


if __name__ == '__main__':
    head = ListNode(1)
    append(head, 2)
    append(head, 3)
    append(head, 4)
    append(head, 5)
    append(head, 6)
    append(head, 7)
    append(head, 8)
    append(head, 9)
    Solution().reorderList(head)
    print_list(head)


