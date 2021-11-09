class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]

# Test if the code above is running correctly
if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert (Solution().twoSum(nums, target) == [0, 1])
    nums = [3, 2, 4]
    target = 6
    assert (Solution().twoSum(nums, target) == [1, 2])
    nums = [3, 3]
    target = 6
    assert (Solution().twoSum(nums, target) == [0, 1])