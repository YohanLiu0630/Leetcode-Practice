#
# @lc app=leetcode id=373 lang=python3
# @lcpr version=30404
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
import heapq

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        pq = []
        res = []
        for i in range(len(nums1)):
            heapq.heappush(pq,(nums1[i]+nums2[0],i,0))
        while pq and k > 0:
            temp, i, j = heapq.heappop(pq)
            k -= 1
            if j + 1 < len(nums2):
                heapq.heappush(pq,(nums1[i] + nums2[j + 1],i,j + 1))
            res.append([nums1[i],nums2[j]])
        return res
# @lc code=end



#
# @lcpr case=start
# [1,7,11]\n[2,4,6]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2]\n[1,2,3]\n2\n
# @lcpr case=end

#

