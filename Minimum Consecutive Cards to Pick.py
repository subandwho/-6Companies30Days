    def minimumCardPickup(self, cards: List[int]) -> int:
        hxmap = {}
        lengths = []
        for i, j in enumerate(cards):
            if j in hxmap:
                lengths.append(abs(hxmap[j]-i)+1)
                hxmap[j] = i
            else:
                hxmap[j] = i
        if len(lengths) > 0:
            return min(lengths)
        else:
            return -1
