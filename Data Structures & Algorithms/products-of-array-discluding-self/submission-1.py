
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix * nums[i]

        suffix = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix = suffix * nums[i]

        return result


        