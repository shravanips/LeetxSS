class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # a path always contain m + n - 1 cells
        # valid parentheses str must then have even len
        if (m + n - 1) % 2 == 1:
            return False

        # val str must start with "(" and end with ")"
        if grid[0] [0] == ")" or grid[m - 1][n - 1] == "(":
            return False
        
        memo = {}

        def dfs(row, col, balance):
            # "(" increase bal
            # ")" decrease bal
            if grid[row][col] == "(":
                balance += 1
            else:
                balance -= 1
            
            # many ")" means this path can never become valid
            if balance < 0:
                return False
            
            # when reached bottom - right cell 
            if row == m - 1 and col == n - 1:
                return balance == 0
            
            # if we already solved the exact situation - return the answer
            state = (row, col, balance)

            if state in memo:
                return memo[state]
            
            # lets try moving down
            go_down = False
            if row + 1 < m:
                go_down = dfs(row + 1, col, balance)
            
            # move right
            go_right = False
            if col + 1 < n:
                go_right = dfs(row, col + 1, balance)
            
            # now we only need one valid path
            memo[state] = go_down or go_right

            return memo[state]
        
        return dfs(0, 0, 0)

#             current cell
#                      |
#              update balance
#                      |
#              balance < 0?
#                /          \
#              YES           NO
#               |             |
#             False       destination?
#                           /       \
#                         YES        NO
#                          |          |
#                    balance==0?   try moves
#                                   /       \
#                                DOWN      RIGHT
#                                  \       /
#                                    OR
#                                     |
#                                True/False
