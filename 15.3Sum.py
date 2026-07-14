class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if v > 0: break
            if i and v == nums[i-1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = v + nums[l] + nums[r]
                if s < 0: l += 1
                elif s > 0: r -= 1
                else:
                    res.add((v, nums[l], nums[r]))
                    l, r = l + 1, r - 1
        return list(res)