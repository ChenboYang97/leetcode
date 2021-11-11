import math
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        def findBestSubarray(left, right, nums):
            # Base case
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            best_left_sum = best_right_sum = 0

            # Best sum for the crossing situation
            # Compute the largest from mid to left
            # Then calculate the largest from mid to right
            # Finally, sum all three items
            curr = 0
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(curr, best_left_sum)
            curr = 0
            for i in range(mid + 1, right + 1, 1):
                curr += nums[i]
                best_right_sum = max(curr, best_right_sum)
            best_cross_sum = best_left_sum + nums[mid] + best_right_sum

            # Best sum for the left situation
            best_left = findBestSubarray(left, mid - 1, nums)
            # Best sum for the right situation
            best_right = findBestSubarray(mid + 1, right, nums)

            best_sum = max(best_left, best_cross_sum, best_right)

            return best_sum

        left = 0
        right = len(nums) - 1
        max_result = findBestSubarray(left, right, nums)

        return max_result

# Test if the code above is running correctly
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    assert (Solution().maxSubArray(nums) == 6)
    nums = [1]
    assert (Solution().maxSubArray(nums) == 1)
    nums = [5,4,-1,7,8]
    assert (Solution().maxSubArray(nums) == 23)
