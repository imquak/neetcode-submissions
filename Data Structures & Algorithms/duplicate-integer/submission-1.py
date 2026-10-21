class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found_numbers = []
        for num in nums:
            if num not in found_numbers:
                found_numbers.append(num)
            else:
                return True
        return False
            
        
        