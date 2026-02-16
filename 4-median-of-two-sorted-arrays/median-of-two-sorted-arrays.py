from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        m, n = len(A), len(B)

        # Always binary search the smaller array
        if m > n:
            A, B = B, A
            m, n = n, m

        total = m + n
        half = (total + 1) // 2

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i

            A_left  = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i]     if i < m else float("inf")
            B_left  = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j]     if j < n else float("inf")

            # Correct partition
            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 1:
                    return float(max(A_left, B_left))
                return (max(A_left, B_left) + min(A_right, B_right)) / 2.0

            # Move partition
            if A_left > B_right:
                hi = i - 1
            else:
                lo = i + 1

        # Optional; practically unreachable for valid sorted inputs
        return 0.0
