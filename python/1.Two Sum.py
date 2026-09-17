#
# @lc app=leetcode id=1 lang=python3
# @lcpr version=30404
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        val_to_index = {}
        for i in range(len(nums)):
            need = target - nums[i]
            if need in val_to_index:
                return [val_to_index[need],i]
            val_to_index[nums[i]] = i
        return []
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

