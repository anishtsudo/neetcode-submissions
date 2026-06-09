class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0 #edge case

        l, r = 0, len(height) - 1 #basic two pointer
        maxL, maxR = height[l], height[r] #setting max height variables 
        res = 0 #base case 

        while l < r:
            if maxL < maxR: #while l is less than right update max left pointer with new height 
                l += 1 #move left by one 
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else: 
                r -= 1 #same thing but for the right pointer 
                maxR = max(maxR, height[r]) #update the pointers location and height 
                res += maxR - height[r] #update result
        
        return res


            
        