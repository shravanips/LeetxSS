class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        # empty creation
        answer = []
        # keep the track
        depth = 0

        for char in seq:
            # if we see an opening "("
            if char == "(":
                depth += 1 # level up
                answer.append(depth % 2) # split between 2 grps
            else:  # (")" case)
                answer.append(depth % 2)
                depth -= 1
        
        return answer
        