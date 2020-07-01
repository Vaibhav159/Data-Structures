"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100."""

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        
        self.memo = {}
        if not grid:
            return 0
        
        self.ans = 0        
        return self.dfs(0, 0, grid)

    
    def dfs(self, m, n, grid):
        if m >= len(grid) or n >= len(grid[0]) or grid[m][n] == 1:
            return 0
        
        if m == len(grid) - 1 and n == len(grid[0]) - 1:
            return 1
        
        if (m, n) in self.memo:
            return self.memo[(m,n)]
        else:
            self.memo[(m,n)] = self.dfs(m + 1, n, grid) + self.dfs(m, n + 1, grid)
            return self.memo[(m, n)]
