class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        
        total = x + y + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        
        current = current.next
    
    if carry > 0:
        current.next = ListNode(carry)
    
    return dummy_head.next




l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = addTwoNumbers(l1, l2)
# The result will be a linked list representing [7, 0, 8]
