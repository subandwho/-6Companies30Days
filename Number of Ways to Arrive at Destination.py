    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v,t))
            graph[v].append((u,t))
        
        times = [sys.maxsize]*n
        times[0] = 0
        ways = [0] * n
        ways[0] = 1

        pq = [(0,0)]
        while pq:
            old_t, u = heappop(pq)

            for v,t in graph[u]:
                new_t = old_t + t

                if new_t < times[v]:
                    heappush(pq, (new_t, v))
                    times[v] = new_t
                    ways[v] = ways[u]
                
                elif times[v] == new_t:
                    ways[v] += ways[u]

        return ways[-1] % (10**9 + 7)
