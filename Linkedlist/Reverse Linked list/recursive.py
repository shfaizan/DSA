from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        bonehead = head

        if head.next:
            bonehead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return bonehead


def append(head, value):
    while head.next:
        head = head.next
    head.next = ListNode(value)


def print_list(head):
    while head:
        print(head.val)
        head = head.next



if __name__ == "__main__":
    head = ListNode(1)
    head_list = [2, 3, 4, 5]
    for elem in head_list:
        append(head, elem)
    sol = Solution()
    reversed_head = sol.reverseList(head)
    print_list(reversed_head)