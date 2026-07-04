class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        char_map = {}
        max_length = 0
        left = 0  # Left pointer of the window
        
        # Loop through the string with the right pointer
        for right, char in enumerate(s):
            # If the character is already in the map and its index is inside the current window
            if char in char_map and char_map[char] >= left:
                # Move the left pointer to the right of the last seen position
                left = char_map[char] + 1
            
            # Update the last seen position of the character
            char_map[char] = right
            
            # Calculate the current window size and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length