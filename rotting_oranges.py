from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid == None or len(grid) == 0:
            return 0
        q = Queue()
        fresh = 0
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.put([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        lvl = 0
        while not q.empty():
            size = q.qsize()
            for i in range(size):
                curr = q.get()
                for Dir in dirs:
                    nr = Dir[0] + curr[0]
                    nc = Dir[1] + curr[1]
                    if nr >=0 and nr < m and nc >= 0 and nc < n and grid[nr][nc] == 1:
                        q.put([nr,nc])
                        fresh = fresh -1
                        grid[nr][nc] = 2
            lvl = lvl + 1
        if fresh != 0:
            return -1
        return lvl - 1

# Time complexity: O(m*n)
# Space complexity: O(m*n)