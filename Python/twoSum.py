class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        num_map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if num_map.get(difference) is not None:
                return [num_map.get(difference), i]
            else:
                num_map[nums[i]] = i
