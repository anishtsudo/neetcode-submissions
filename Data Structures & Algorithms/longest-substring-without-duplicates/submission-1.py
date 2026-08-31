class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setlen = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in setlen:
                setlen.remove(s[l])
                l += 1
            setlen.add(s[r])
            res = max(res, r - l + 1)
        return res


            
