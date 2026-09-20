#
# @lc app=leetcode id=19 lang=python3
# @lcpr version=30404
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(-1)
        dummy.next = head
        fast = head
        slow = head
        pre = dummy
        for i in range(n):
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
            pre = pre.next
        pre.next = slow.next
        slow = None
        return dummy.next
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n1\n
# @lcpr case=end

#

