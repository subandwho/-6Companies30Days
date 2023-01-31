    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
        j = 0
        for i in range(1,n):
            while s[i] != s[j] and j > 0:
                j = lps[j-1]

            if s[i] == s[j]:
                lps[i] = j+1
                j += 1
        
        return s[:lps[-1]]
