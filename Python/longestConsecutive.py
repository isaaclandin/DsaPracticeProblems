class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_map = {}
        longest = 0
        nums.sort()
        print(nums)

        for num in nums:
            print("current num: " + str(num))
            if not nums:
                return 0
            if len(nums) == 1:
                return 1
            print(num_map.get(num-1, 0))
            if num_map.get(num-1, 0) == 0:
                num_map.update({num: 1})
                if longest == 0:
                    longest += 1
            else:
                temp = (num_map.get(num-1, 0) + 1) 
                num_map.update({num: temp})
                if temp > longest:
                    longest = temp
            print("current longest: " + str(longest))

        return longest
