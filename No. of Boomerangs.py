    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dist(x,y):
            return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
        
        count=0
        for p in points:
            
            dic = {}
            for q in points:


                dis = dist(p,q)
                dic[dis] = dic.get(dis,0) + 1
            for k in dic:
                count += dic[k] * (dic[k]-1)
        return count
