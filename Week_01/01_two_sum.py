#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = nums.copy()
        temp.sort()
        i = 0
        j = len(temp) - 1
        while (i < j):
            if (temp[i] + temp[j] < target):
                i += 1
            elif (temp[i] + temp[j] > target):
                j -= 1
            else:
                break
        p = nums.index(temp[i])
        nums.pop(p)
        q = nums.index(temp[j])
        if q >= p:
            q += 1
        return [p, q]

# @lc code=end
