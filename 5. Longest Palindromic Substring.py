class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 1:
            return ""
        
        start, end = 0, 0
        
        def expand_around_center(left: int, right: int) -> int:
            # Expand outward as long as characters match and indices are within bounds
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the length of the palindrome found
            return right - left - 1

        for i in range(len(s)):
            # Case 1: Odd length palindrome centered at i (e.g., "aba")
            len1 = expand_around_center(i, i)
            # Case 2: Even length palindrome centered between i and i+1 (e.g., "abba")
            len2 = expand_around_center(i, i + 1)
            
            # Find the maximum length between the two cases
            max_len = max(len1, len2)
            
            # Update the start and end pointers if a longer palindrome is found
            if max_len > end - start:
                # Calculate new boundaries based on the current center i
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                
        return s[start:end + 1]