from collections import deque, defaultdict
cache = defaultdict(int)
def count_hexagonal_paths(n):
    directions = [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]
    
    
    def bfs(start):
        queue = deque([(start, 0)])  
        count = 0
        
        while queue:
            (x, y), steps = queue.popleft()
            if steps < n:
                for dx, dy in directions:
                    new_x, new_y = x + dx, y + dy
                    if (new_x, new_y, steps + 1) not in cache:
                        queue.append(((new_x, new_y), steps + 1))
                    cache[(new_x, new_y, steps + 1)] += cache[(x, y, steps)]
        return count
    
    return bfs((0, 0))


numTimes = int(input())
tests = []
memo = {}
for i in range(numTimes):
    tests.append(int(input()))
for i in range(numTimes):
    count_hexagonal_paths(tests[i])
    print(cache[(0, 0, tests[i])])

