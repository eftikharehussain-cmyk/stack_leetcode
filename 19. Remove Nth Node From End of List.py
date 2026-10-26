# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        cur = ListNode(0)
        cur.next = head
        first_pointer = cur
        second_pointer = cur
        for _ in range(n + 1):
            first_pointer = first_pointer.next
        while first_pointer:
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next
        deleteNode = second_pointer.next
        second_pointer.next = deleteNode.next
        deleteNode.next = None
        return cur.next
        