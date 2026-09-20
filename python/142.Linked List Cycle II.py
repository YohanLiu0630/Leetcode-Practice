#
# @lc app=leetcode id=142 lang=python3
# @lcpr version=30404
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pfast = head
        pslow = head
        while pfast is not None and pfast.next is not None:
            pfast = pfast.next.next
            pslow = pslow.next
            if pslow == pfast:
                pslow = head
                while pslow != pfast:
                    pfast = pfast.next
                    pslow = pslow.next
                return pslow
        return None
# @lc code=end



#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#

