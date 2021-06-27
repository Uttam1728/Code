# Longest Common Subsequence | Finding all LCS

# Function to find the longest common subsequence of string `X[0…m-1]` and `Y[0…n-1]`
def LCS(X, Y):
	l1, l2 = len(X), len(Y)
	dp = [[0]*(l2+1) for i in range(l1+1)]
	LCSLengthBottamUp(X, Y, dp)	
	
	def helper(i,j,ans,curr):
		print((i,j,ans,curr))
		if i <= 0 or j <= 0:
			ans.append(curr)
			return
		if X[i-1] == Y[j-1]:
			helper(i-1,j-1,ans,X[i-1] + curr)
		else:
			if left >= right:
				helper(i,j-1,ans,curr)
			if right >= left:
				helper(i-1,j,ans,curr)
		
	
	
	ans = []
	helper(l1,l2,ans,"")
	return ans
	

def LCSLengthBottamUp(X, Y, dp):
	l1, l2 = len(X), len(Y)
	if not dp:
		dp = [[0]*(l2+1) for i in range(l1+1)]
	# print(dp)
	for i in range(1,l1+1):
		for j in range(1,l2+1):
			if X[i-1] == Y[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i][j-1],dp[i-1][j])
	for i in dp:
		print(i,"dp")
	return dp
	# return dp[l1][l2]


if __name__ == '__main__':

	X = "ABCBDAB"
	Y = "BDCABA"


	# find the longest common sequence
	print(LCS(X, Y))
