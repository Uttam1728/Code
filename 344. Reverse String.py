'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverseStringByIteration(s):
            if not s : return None

            l,h = 0, len(s)-1

            while l < h:
                s[l], s[h] = s[h], s[l]

                l += 1
                h -= 1
        def reverseStringByInBuiltFun(s):
            s[:] = s[::-1]
        def reverseStringByRecursion(s):
            def helper(l, r):
                if l < r :
                    s[l], s[r] = s[r], s[l]
                    helper(l+1,r-1)

            if not s : return 
            helper(0,len(s)-1)
            
        reverseStringByIteration(s)
        # reverseStringByInBuiltFun(s)
        # reverseStringByRecursion(s)
