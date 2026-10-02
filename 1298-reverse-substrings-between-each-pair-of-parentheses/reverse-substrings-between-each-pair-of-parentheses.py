class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current = ""

        for char in s:
            # opening parenthesis - first save what we have built before it
            if char == "(":
                stack.append(current)
                current = ""

            # Closing parenthesis
            # reverse what was inside the paretheses and see what came before
            elif char == ")":
                previous = stack.pop()
                current = previous + current[::-1]

            # nomral letter: add it to the current str
            else:
                current += char
                    
        return current