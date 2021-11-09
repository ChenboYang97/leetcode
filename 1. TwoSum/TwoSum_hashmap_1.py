class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create an empty dictionary
        # Make numbers being the keys and indexes being the values
        key_num = {}
        for value, key in enumerate(nums):
            if key in key_num:
                key_num[key].append(value)
            else:
                key_num[key] = [value]

        for i in range(len(nums)):
            next_num = target - nums[i]
            # Check if the number is half of the target
            # If so, if there exist another number which has the same value, then return directly
            if next_num == nums[i]:
                if len(key_num[next_num]) >= 2:
                    return [i, key_num[next_num][1]]
                else:
                    continue

            # Check if the number was stored in the dictionary
            # If so, return it
            # Otherwise, continue to the next number
            if next_num in key_num:
                return [i, key_num[next_num][0]]

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