class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        init_start = 1
        start = 1
        index = 0
        length = len(nums)
        while (index < length):
            sum_temp = start + nums[index]
            if sum_temp < 1:
                init_start += 1-sum_temp
                start += 1-sum_temp
                continue
            else:
                start = start+nums[index]
                index += 1
        return init_start

if __name__ == '__main__':
    nums = [-3, 2, -3, 4, 2]
    assert(Solution().minStartValue(nums) == 5)
    nums = [1, 2]
    assert(Solution().minStartValue(nums) == 1)
    nums = [1, -2, -3]
    assert(Solution().minStartValue(nums) == 5)
