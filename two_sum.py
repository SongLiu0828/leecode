class Solution(object):
    def twoSum(self, nums, target):
        for num_one in nums:
            if target-num_one in nums and num_one is not target-num_one:
                return [nums.index(num_one), nums.index(target - num_one)]

nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums, target))
