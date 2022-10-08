# // Time Complexity : O(n)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this :
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        
        #find middle of the list
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next

        #reverse the second half
        head2 = self.reverseList(slow.next)
        slow.next = None
        
        #reorder list
        p1 = head
        temp = p1.next
        p2 = head2
        
        while(p2):
            p1.next = p2
            p2 = p2.next
            p1.next.next = temp
            p1 = temp
            if temp:
                temp = temp.next
                
            
    def reverseList(self, head: Optional[ListNode]):
        if not head or not head.next:
            return head
        prev = None
        cur = head
        while(cur):
            temp = cur.next 
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev
        