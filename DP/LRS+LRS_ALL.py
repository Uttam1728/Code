'''
The problem is finding Given a string, find the length of 
the longest repeating subsequence such that the two subsequences 
don’t have same string character at the same position, 
i.e., any i’th character in the two subsequences shouldn’t have the same index in the original string. 

'''



def LRSLengthTopDown(X):
	cache = {}
	l1 = len(X)
	
	def helper(i,j):
		# print(i,j,l1,l2)
		if i == l1 or j == l1:
			return 0
		key = (i,j)
		
		if key not in cache :
			if X[i] == X[j] and i != j:
				cache[key]= 1 + helper(i+1,j+1)
			else:
				cache[key]= max(helper(i+1,j),helper(i,j+1))
			
		return cache[key]
		
	return helper(0,0)
	
def LRSLengthBottamUp(X,dp = None):
	l1 = len(X)
	if not dp:
		dp = [[0]*(l1+1) for i in range(l1+1)]
	
	for i in range(1,l1+1):
		for j in range(1,l1+1):
			if X[i-1] == X[j-1] and i != j:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i][j-1],dp[i-1][j])
	for i in dp:
		print(i)
	return dp[l1][l1]
	
def LRS_All(X):
	l1 = len(X)
	dp = [[0]*(l1+1) for i in range(l1+1)]
	LRSLengthBottamUp(X,dp)
	
	def helper(i,j,ans,curr):
		if i <= 0 or j <= 0:
			ans.append(curr)
			return
		if X[i-1] == X[j-1] and i != j:
			return helper(i-1,j-1,ans,X[i-1] + curr)
		if dp[i-1][j] >= dp[i][j-1]:
			return helper(i-1,j,ans,curr)
		if dp[i][j-1] >= dp[i-1][j]:
			return helper(i,j-1,ans,curr)
	
	
	
	ans = []
	helper(l1,l1,ans,"")
	return ans

if __name__ == '__main__':

	# X = "ATACTCGGA"
	X = "AABEBCDD"
	# create a dictionary to store solutions to subproblems
	lookup = {}

	print("The length of the longest repeating subsequence is", LRSLengthTopDown(X))
	print("The length of the longest repeating subsequence is", LRSLengthBottamUp(X))
	print("the longest repeating subsequence is", LRS_All(X))


