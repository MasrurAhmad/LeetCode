class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted_half = 0
        
        # Loop until we reach the middle of the number
        while x > reverted_half:
            # Shift reverted_half by 1 digit to the left and add the last digit of x
            reverted_half = reverted_half * 10 + x % 10
            # Remove the last digit from x
            x //= 10
            
        # For even length, x == reverted_half
        # For odd length, x == reverted_half // 10 (ignores the middle digit)
        return x == reverted_half or x == reverted_half // 10