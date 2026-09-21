#
# @lc app=leetcode id=204 lang=python3
# @lcpr version=30404
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        is_prime=[True]*n
        is_prime[0]=False
        is_prime[1]=False
        i=2
        while i*i<n:
            if is_prime[i]:
                is_prime[i*i:n:i]=[False]*(((n-1-i*i)//i)+1)
            i+=1
        return sum(is_prime)
# @lc code=end



#
# @lcpr case=start
# 10\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 1\n
# @lcpr case=end

#

