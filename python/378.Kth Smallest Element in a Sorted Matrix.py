#
# @lc app=leetcode id=378 lang=python3
# @lcpr version=30404
#
# [378] Kth Smallest Element in a Sorted Matrix
#


# @lc code=start
# from queue import PriorityQueue
import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        # pq = PriorityQueue()
        # for i in range(len(matrix)):
        #     pq.put((matrix[i][0],i,0))

        # while not pq.empty() and k > 0:
        #     cur = pq.get()
        #     res = cur[0]
        #     k -= 1
        #     i , j = cur[1], cur[2]
        #     if j + 1 < len(matrix[i]):
        #         pq.put((matrix[i][j+1],i,j+1))
        # return res
        
        
        pq = []
        for i, head in enumerate(matrix):
            heapq.heappush(pq,(head[0],i,0))
        while pq and k > 0:
            res,i,j = heapq.heappop(pq)
            k -= 1
            if j + 1 < len(matrix[i]):
                heapq.heappush(pq,(matrix[i][j+1],i,j+1))
        return res
# @lc code=end



#
# @lcpr case=start
# [[1,5,9],[10,11,13],[12,13,15]]\n8\n
# @lcpr case=end

# @lcpr case=start
# [[-5]]\n1\n
# @lcpr case=end

#

