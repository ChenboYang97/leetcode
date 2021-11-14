import math

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start = 0
        sum_subarray = 0
        length = 0
        min_length = math.inf

        for end in range(len(nums)):
            sum_subarray += nums[end]
            end += 1

            while sum_subarray >= target:
                length = end - start
                min_length = min(min_length, length)
                sum_subarray -= nums[start]
                start += 1

        if min_length == math.inf:
            return 0
        else:
            return min_length

if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    assert(Solution().minSubArrayLen(target,nums) == 2)
    target = 4
    nums = [1, 4, 4]
    assert(Solution().minSubArrayLen(target,nums) == 1)
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    assert(Solution().minSubArrayLen(target,nums) == 0)
