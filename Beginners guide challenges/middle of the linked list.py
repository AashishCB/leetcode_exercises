from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node_v1(head: Optional[ListNode]):
    count = 1
    temp = head
    while temp.next is not None:
        temp = temp.next
        count += 1
    middle = count // 2
    temp = head
    count = 0
    while count != middle:
        temp = temp.next
        count += 1
    print(temp.val)


def middle_node(head: Optional[ListNode]):
    middle = head
    end = head
    while end and end.next is not None:
        middle = middle.next
        end = end.next.next
    print(middle.val)


def insert_data_from_array(nums):
    top = ListNode(nums[-1])
    for i in range(len(nums) - 2, -1, -1):
        top = ListNode(nums[i], top)
    return top


middle_node(head=insert_data_from_array([1, 2, 3, 4, 5]))
middle_node(head=insert_data_from_array([1, 2, 3, 4, 5, 6]))


# e = ListNode(5)
# d = ListNode(4, e)
# c = ListNode(3, d)
# b = ListNode(2, c)
# a = ListNode(1, b)

# print(a.next.next.val)
