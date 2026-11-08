class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if a > 0:                      # sorted: no way to reach 0 anymore
                break
            if i > 0 and a == nums[i - 1]: # skip duplicate first numbers
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = a + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:  # skip duplicate seconds
                        l += 1
        return res