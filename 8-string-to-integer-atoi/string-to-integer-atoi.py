class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        sign = 1
        num = 0

        # Skip spaces
        while i < len(s) and s[i] == " ":
            i += 1

        # Check + or -
        if i < len(s) and s[i] == "-":
            sign = -1
            i += 1
        elif i < len(s) and s[i] == "+":
            i += 1
        
        # Read digits
        while i < len(s) and "0" <= s[i] <= "9":
            digit = ord(s[i]) - ord("0")
            num = num * 10 + digit
            i += 1
        
        # Apply sign
        num = sign * num

        # Keep number inside 32 bit range
        INT_MIN = -(2 ** 31)
        INT_MAX = 2 ** 31 - 1

        if num < INT_MIN:
            return INT_MIN

        if num > INT_MAX:
            return INT_MAX
        
        return num
        