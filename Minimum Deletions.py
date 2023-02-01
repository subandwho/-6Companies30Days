    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        g = gcd(*numsDivide)
        for i, a in enumerate(sorted(nums)):
            if g % a == 0: 
                return i
            if g < a:
                break
        return -1
