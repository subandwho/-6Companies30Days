    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        res = 2

        for i in range(len(points)):
            dic = defaultdict(int)

            for j in range(i+1,len(points)):

                    if points[j][0] - points[i] [0] == 0:
                        dic[float('inf')] += 1
                    else:
                        dic[((points[j][1]- points[i][1])/ (points[j][0]-points[i][0]))] += 1
            if dic.values():
             res = max(res, max(dic.values())+1)

        return res
