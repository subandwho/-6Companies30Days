    def getHint(self, secret: str, guess: str) -> str:
        bucket = [0] * 10
        bull, cow = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                bull += 1
            else:
                bucket[int(s)] += 1
                bucket[int(g)] -= 1
        cow = len(secret) - bull - sum([x for x in bucket if x > 0])
        return f'{bull}A{cow}B'
