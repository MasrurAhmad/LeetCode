class Solution:
    def myAtoi(self, s: str) -> int:
        # Define 32-bit signed integer boundaries
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        i = 0
        n = len(s)
        
        # Step 1: Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1
            
        # Step 2: Check for sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1  # Move past the sign character
            
        # Step 3: Convert digits
        result = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = result * 10 + digit
            i += 1
            
        # Apply the sign
        result *= sign
        
        # Step 4: Handle rounding/clamping
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
            
        return result