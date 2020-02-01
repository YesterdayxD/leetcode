# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummyNode = ListNode(0)
        dummyNode.next = head
        first = dummyNode
        second = dummyNode

        for i in range(1, n + 2):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummyNode.next
