class Solution:
    def minStartValue(self, nums: list[int]) -> int:        
        init_start = 1
        start = 1
        index = 0
        
        while (index < len(nums)):
            start += nums[index]
            if start < 1:
                init_start += 1 - start
                start = 1
            index += 1
            
        return init_start

if __name__ == '__main__':
    nums = [-3,2,-3,4,2]
    assert(Solution().minStartValue(nums) == 5)
    nums = [1,2]
    assert(Solution().minStartValue(nums) == 1)
    nums = [1,-2,-3]
    assert(Solution().minStartValue(nums) == 5)
