# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another 
# sequence by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = {}
        
        def helperMem(l,h):
            key = (l, h)
            if key in cache : return cache[key]
            if l > h : return 0
            if l == h : return 1
            if s[l] == s[h]:
                cache[key] = 2 + helperMem(l+1, h-1)
            else:
                cache[key] =  max(helperMem(l, h-1), helperMem(l+1, h))
            return cache[key]
        
       
        def helperMemFull(l,h):
            key = (l, h)
            if key in cache : return cache[key]
            if l > h : return ''
            if l == h : return s[l]
            if s[l] == s[h]:
                cache[key] = s[l] + helperMemFull(l+1, h-1) + s[l]
            else:
                cache[key] =  max(helperMemFull(l, h-1), helperMemFull(l+1, h), key = len)
            return cache[key]
	    

#             if len(s) < 2 : return s 
#             return helperMemFull(0, len(s)-1)


        if len(s) < 2 : return len(s) 
        return helperMem(0, len(s)-1)
