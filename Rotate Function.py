    def maxRotateFunction(self, nums: List[int]) -> int:
        r = curr = sum(idx * ele for idx, ele in enumerate(nums))
        s = sum(nums)
        k = len(nums)
        while nums:
            curr += s - nums.pop() * k
            r = max(curr, r)
        return r 
            
