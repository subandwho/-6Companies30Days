    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        delta = [a-b for a,b in zip(nums1, nums2)]
        aux = []
        res = 0
        for y in delta:
            cnt = bisect.bisect_right(aux, y+diff)
            res += cnt
            bisect.insort(aux, y)
        
        return res
