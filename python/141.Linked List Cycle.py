#
# @lc app=leetcode id=141 lang=python3
# @lcpr version=30404
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pfast = head
        pslow = head
        while pfast is not None and pfast.next is not None:
            pslow = pslow.next
            pfast = pfast.next.next
            if pslow == pfast:
                return True
        return False
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

