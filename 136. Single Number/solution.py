class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        array = []
        for i in range(0, len(nums)):
            if nums[i] in array:
                array.remove(nums[i])
            else:
                array.append(nums[i])
        return array[0]