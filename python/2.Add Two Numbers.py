#
# @lc app=leetcode id=2 lang=python3
# @lcpr version=30404
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        p = dummy
        p1 = l1
        p2 = l2
        carry = 0
        while p1 is not None or p2 is not None or carry > 0:
            val = carry
            if p1 is not None:
                val += p1.val
                p1 = p1.next
            if p2 is not None:
                val += p2.val
                p2 = p2.next
            carry = val //10
            val = val % 10
            p.next = ListNode(val)
            p = p.next
        return dummy.next
# @lc code=end


#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

