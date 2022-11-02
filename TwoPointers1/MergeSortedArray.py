#Time_Complexity: O(n) 
#Space_Complexity : O(1)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m-1     # Create first pointer to m-1 
        second = n-1    # Create second pointer to n-1
        third = m+n-1   # Create third pointer to m+n-1
        
        while first >= 0 and second >= 0: # run until the first and second pointers are greater than 0
            if nums1[first] < nums2[second]: # if the nums1[first] is less than nums2[second] 
                nums1[third] = nums2[second] # change nums1[third] with nums2[second]
                second -= 1 # decrement second by 1
            
            else: 
                nums1[third] = nums1[first] # change nums1[third] with nums1[first]
                first -= 1  # decrement first by 1
            third -= 1  # decrement third by 1

        if second >=0:  # if the second is greater than or equal to 0
            nums1[:second+1] = nums2[:second+1] # copy all the elements in nums2 to nums1
