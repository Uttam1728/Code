'''

Sum of array elements using recursion
Difficulty Level : Basic
Last Updated : 12.02.2021
Given an array of integers, find sum of array elements using recursion.

'''

# function
    
def sumOfArrayIterative(nums, l):
    ans = 0
    for i in range(l):
        ans += nums[i]
    ### If Length is not there
    # for i in nums:
    #     ans += i
    return ans
    
def sumOfArrayIterativeRecursive(nums, l):
    if not l : return 0
    return nums[l-1] + sumOfArrayIterativeRecursive(nums, l-1)
    ### If Length is not there
    # if not nums : return 0
    # return nums[0] + sumOfArrayIterativeRecursive(nums[1:]) 
    
# driver Code

v1 = sumOfArrayIterative([100,1,43,7,45,98,13,78])
print(v1)
 
v2 = sumOfArrayIterativeRecursive([100,1,43,7,45,98,13,78])
print(v2)

# LeetCode PlayGround Or Question Link

'''
https://leetcode.com/playground/5EKcBuRv/live
'''
