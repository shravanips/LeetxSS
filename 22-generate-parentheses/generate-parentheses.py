class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        # current  - parentheses we built so far
        # open_count - number of "(" used
        # close_count - number of ")" used
        def backtrack(current, open_count, close_count):
            # used all n pairs
            if len(current) == 2 * n:
                result.append(current)
                return

            
            # add "(" uf we still have something available
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            
            # add ")" only if it can match existing "("
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        
        backtrack("", 0, 0)

        return result

        