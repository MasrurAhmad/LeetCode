class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            # Get values, default to 0 if list is exhausted
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = v1 + v2 + carry
            carry = total // 10
            
            # Add new node to the result list
            current.next = ListNode(total % 10)
            
            # Move pointers forward
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy_head.next