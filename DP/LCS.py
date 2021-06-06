'''
The Longest Common Subsequence (LCS) problem is finding the longest subsequence present in given two sequences in the same order,
i.e., find the longest sequence which can be obtained from the first original sequence by deleting some items and from the second original sequence
by deleting other items.

'''





# Function to find the length of the longest common subsequence of substring
# `X[0…m-1]` and `Y[0…n-1]`
def LCSLengthTopDown(X, Y):
	cache = {}
	l1, l2 = len(X), len(Y)
	
	def helper(i,j):
		# print(i,j,l1,l2)
		if i == l1 or j == l2:
			return 0
		key = (i,j)
		
		if key not in cache :
			if X[i] == Y[j]:
				cache[key]= 1 + helper(i+1,j+1)
			else:
				cache[key]= max(helper(i+1,j),helper(i,j+1))
			
		return cache[key]
		
	return helper(0,0)
	
def LCSLengthBottamUp(X, Y):
	l1, l2 = len(X), len(Y)
	dp = [[0]*(l2+1) for i in range(l1+1)]
	
	for i in range(1,l1+1):
		for j in range(1,l2+1):
			if X[i-1] == Y[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i][j-1],dp[i-1][j])
	for i in dp:
		print(i)
	return dp[l1][l2]
	
	
def LCSLengthBottamUpSpaceOptimizedTwoArray(X, Y):
	l1, l2 = len(X), len(Y)
	if l2 > l1:
		LCSLengthBottamUpSpaceOptimizedTwoArray(Y, X)
	prev = [0]*(l2+1)
	curr = [0]*(l2+1)
	for i in range(1,l1+1):
		for j in range(1,l2+1):
			if X[i-1] == Y[j-1]:
				curr[j] = 1 + prev[j-1]
			else:
				curr[j] = max(curr[j-1], prev[j])
		print(prev)
		# print(curr)
		prev = curr.copy()
		
	
	return curr[l2]	
	
def LCSLengthBottamUpSpaceOptimizedOneArray(X, Y):
	l1, l2 = len(X), len(Y)
	if l2 > l1:
		LCSLengthBottamUpSpaceOptimizedOneArray(Y, X)
		
	curr = [0]*(l2+1)
	
	for i in range(1,l1+1):
		prev = curr[0]
		
		for j in range(1,l2+1):
			backup = curr[j]
			if X[i-1] == Y[j-1]:
				curr[j] = 1 + prev
			else:
				curr[j] = max(curr[j-1], backup)
			prev = backup
		print(curr)
		
		
	
	return curr[l2]			
	


if __name__ == '__main__':

	X = "ABCBDAB"
	Y = "BDCABA"

	# create a dictionary to store solutions to subproblems
	lookup = {}

	print("The length of the LCS is", LCSLengthTopDown(X, Y))
  print("The length of the LCS is", LCSLengthBottamUp(X, Y))
  print("The length of the LCS is", LCSLengthBottamUpSpaceOptimizedTwoArray(X, Y))
  print("The length of the LCS is", LCSLengthBottamUpSpaceOptimizedOneArray(X, Y))
