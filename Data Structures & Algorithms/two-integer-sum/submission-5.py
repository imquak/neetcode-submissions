class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index_i,i in enumerate(nums):
            looking_for = target-i
            for index_j,j in enumerate(nums[index_i+1:]):
                if j == looking_for:
                    return [index_i,index_j + index_i + 1]
            nums[:-1]
        return None