class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        print('input',nums1,nums2)
        arr = nums1 + nums2
        arr.sort()
        n = len(arr)
        
        if n % 2 == 0:
            z = n // 2
            e = arr[z]
            q = arr[z - 1]
            ans = (e + q) / 2
            ans=format(ans,'.5f')
            return ans
         
        # If length of array is odd
        else:
            z = n // 2
            ans = arr[z]
            ans=format(ans,'.5f')
            return ans
        
c=Solution()

print('output',c.findMedianSortedArrays([1,2,3],[4,5]))

        
