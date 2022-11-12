class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):

            secondnum = target - nums[i]
            if secondnum in map:
                return [i, map[secondnum]]
            
            map[nums[i]] = i