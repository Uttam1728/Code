'''
Program for factorial of a number
Difficulty Level : Basic
Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n. For example factorial of 6 is 6*5*4*3*2*1 which is 720.
'''

def factIterative(num):
    ans = 1
    for i in range(2,num+1):
        ans *= i
    return ans
    
def factRecursive(num):
    # One Liner
    # return 1  if num == 0 else num * factRecursive(num-1)
    if num == 1 : return 1
    return num * factRecursive(num-1)

v1 = factIterative(100)
 
v2 = factRecursive(100)


'''
https://leetcode.com/playground/Bn7Ajbi5/live

'''
