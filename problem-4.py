# // Time Complexity : O(m+n)
# // Space Complexity : O(1)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this :
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        
        lenA = 0
        lenB = 0
        
        #find length of A
        curr = headA
        while curr:
            lenA += 1
            curr = curr.next
            
        #find length of B
        curr = headB
        while curr:
            lenB += 1
            curr = curr.next
            
        while lenA > lenB:
            headA = headA.next
            lenA -= 1
            
        while lenB > lenA:
            headB = headB.next
            lenB -= 1
            
        while not (headA == headB):
            headA = headA.next
            headB = headB.next
        
        return headA