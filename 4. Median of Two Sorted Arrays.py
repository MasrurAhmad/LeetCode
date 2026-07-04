class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = (total + 1) // 2
        
        # Ensure A is the smaller array to optimize binary search time complexity to O(log(min(m, n)))
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A)
        while l <= r:
            i = (l + r) // 2  # Partition index for A
            j = half - i      # Partition index for B
            
            # Handle boundary conditions using infinity values
            Aleft = A[i - 1] if i > 0 else float('-inf')
            Aright = A[i] if i < len(A) else float('inf')
            Bleft = B[j - 1] if j > 0 else float('-inf')
            Bright = B[j] if j < len(B) else float('inf')
            
            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total elements
                if total % 2 != 0:
                    return float(max(Aleft, Bleft))
                # Even total elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
            
            elif Aleft > Bright:
                # We need to shift the partition in A to the left
                r = i - 1
            else:
                # We need to shift the partition in A to the right
                l = i + 1