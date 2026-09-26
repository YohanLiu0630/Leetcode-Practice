#
# @lc app=leetcode id=445 lang=python3
# @lcpr version=30404
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        stk1 = []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        stk2 = []
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        dummy = ListNode(-1)
        carry = 0
        while stk1 or stk2 or carry > 0:
            val = carry
            if stk1:
                val += stk1.pop()
            if stk2:
                val += stk2.pop()
            carry = val // 10
            val = val % 10
            newNode = ListNode(val)
            newNode.next = dummy.next
            dummy.next = newNode
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [7,2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

#

