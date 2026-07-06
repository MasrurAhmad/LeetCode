class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If 1 row or string is too short, no conversion is needed
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Initialize an array of strings for each row
        rows = [""] * numRows
        current_row = 0
        going_down = False
        
        # Distribute characters into their respective rows
        for char in s:
            rows[current_row] += char
            
            # Change direction if we reach the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row based on direction
            current_row += 1 if going_down else -1
            
        # Combine all rows to get the final converted string
        return "".join(rows)