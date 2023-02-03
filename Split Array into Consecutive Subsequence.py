    def isPossible(self, nums: List[int]) -> bool:
        am = Counter(nums)
        vm = defaultdict(int)

        for num in nums:
            if not am[num]:
                continue
            if vm[num-1] > 0:
                vm[num-1] -= 1
                vm[num] += 1
                am[num] -= 1
            
            else:
                if (not am[num+1] or not am[num+2]):
                    return False
                am[num] -= 1
                am[num+1] -= 1
                am[num+2] -= 1
                vm[num+2] += 1
        return True
