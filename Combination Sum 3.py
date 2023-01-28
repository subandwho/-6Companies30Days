    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def sums(i, cur):
            if sum(cur) > n or len(cur) > k:
                return
            if sum(cur) == n and len(cur) == k:
                res.append(cur.copy())
                return 

            for j in range(i, len(nums)):
                el = nums[j]
                sums(j+1, cur+[el])

        res = []
        cur = []
        nums = [i for i in range(1,10)]
        sums(0, [])
        return res 
        
