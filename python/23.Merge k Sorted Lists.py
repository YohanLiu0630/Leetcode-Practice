#
# @lc app=leetcode id=23 lang=python3
# @lcpr version=30404
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self,other):
        return self.val < other.val
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not list:
            return None
        dummy = ListNode(-1)
        p = dummy
        pq = []
        for i , head in enumerate(lists):
            if head is not None:
                heapq.heappush (pq,(head.val, i, head))

        while pq:
            val, i, node = heapq.heappop(pq)
            p.next = node
            if node.next is not None:
                heapq.heappush(pq, (node.next.val, i, node.next))
            p = p.next
        return dummy.next 
# @lc code=end



#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#

