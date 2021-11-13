class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        right = len(nums) - 1
        count = 0

        for left in range(len(nums)):
            if nums[left] == val:
                while left < right:
                    if nums[right] != val:
                        count += 1
                        nums[left] = nums[right]
                        right -= 1
                        break
                    else:
                        right -= 1
            else:
                count += 1

            if left >= right:
                break

        return count


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    assert(Solution().removeElement(nums,val) == 2)
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    assert(Solution().removeElement(nums,val) == 5)

