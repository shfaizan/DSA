from typing import Optional


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def append(ll, value):
    while ll.next:
        ll = ll.next
    ll.next = ListNode(value)
    return


def start_append_single_head(to_append: Optional[list] = None):
    if to_append:
        head = ListNode(to_append[0])
        to_append.pop(0)
        for val in to_append:
            append(head, val)
    else:
        head = ListNode(2)
        append(head, 4)
        append(head, 3)
        # append(head, 4)
        # append(head, 5)
        # append(head, 6)
        # append(head, 7)
    return head


def start_append_multi_head():
    ll1 = start_append_single_head([9, 9, 9, 9, 9, 9, 9])
    ll2 = start_append_single_head([9, 9, 9, 9])
    return ll1, ll2


def print_ll(head):
    while head:
        print(head.val)
        head = head.next


class ListNode1:
    def __init__(self, val=None, next=None, rand=None, idx=None):
        self.idx = idx
        self.val = val
        self.next = next
        self.random = rand


def random_ll_generator():
    null = None
    one = ListNode1(4, null, idx=1)
    ten = ListNode1(3, one, idx=10)
    eleven = ListNode1(2, ten, idx=11)
    thirteen = ListNode1(1, eleven, idx=13)
    seven = ListNode1(0, thirteen, idx=7)
    seven.random = null
    thirteen.random = seven
    eleven.random = one
    ten.random = eleven
    one.random = seven
    head = seven
    return head
