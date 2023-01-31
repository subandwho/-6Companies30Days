    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r and (nums[l] <= nums[l+1] or nums[r] >= nums[r-1]):
            if nums[l] <= nums[l+1]:
                l += 1
            if nums[r] >= nums[r-1]:
                r -=1
        
        if l == r:
            return 0
        
        for idx in range(l, r+1):
            while l-1 >= 0 and nums[idx] < nums[l-1]:
                l -= 1
            
            while r+1 < len(nums) and nums[idx] > nums[r+1]:
                r += 1
        
        return (r-l+1)
