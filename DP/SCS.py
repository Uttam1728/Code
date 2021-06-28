# Function to display the differences between two strings


def LCS_LengthBottamUp(X, Y,dp = None):
	l1, l2 = len(X), len(Y)
	if not dp:
		dp = [[0]*(l2+1) for i in range(l1+1)]
	
	for i in range(1,l1+1):
		for j in range(1,l2+1):
			if X[i-1] == Y[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = max(dp[i][j-1],dp[i-1][j])
	for i in dp:
		print(i)
	# return dp[l1][l2]

def SCS_LengthBottamUp(X,Y,dp = None):
	l1, l2 = len(X), len(Y)
	if not dp:
		dp = [[0]*(l2+1) for i in range(l1+1)]
	
	for i in range(l1+1):
		for j in range(l2+1):
			if i == 0 or j == 0:
				dp[i][j] = i + j
			
			elif X[i-1] == Y[j-1]:
				dp[i][j] = 1 + dp[i-1][j-1]
			else:
				dp[i][j] = min(dp[i][j-1]+1,dp[i-1][j]+1)
	for i in dp:
		print(i)
	return dp[l1][l2]	

	
def SCS_By_LCS_ALL(X,Y):
	l1, l2 = len(X), len(Y)
	dp = [[0]*(l2+1) for i in range(l1+1)]
	
	LCSLengthBottamUp(X,Y,dp)


	def helper(i,j,ans,curr):
		# print(i,j,ans,curr)
		if i <= 0 and j <= 0:
			ans.append(curr)
			return
		if i > 0 and j > 0 and X[i-1] == Y[j-1]:
			return helper(i-1,j-1,ans,X[i-1]+curr)
			
		if j > 0 and (i == 0 or dp[i][j-1] >= dp[i-1][j]):
			helper(i,j-1,ans,Y[j-1]+curr)
		if i > 0 and(j == 0 or dp[i-1][j] >= dp[i][j-1]):
			helper(i-1,j,ans,X[i-1]+curr)
		
	ans = []
	helper(l1,l2,ans,"")
	return ans

def SCS_ALL(X,Y):
	l1, l2 = len(X), len(Y)
	dp = [[0]*(l2+1) for i in range(l1+1)]
	
	SCS_LengthBottamUp(X,Y,dp)


	def helper(i,j,ans,curr):
		# print(i,j,ans,curr)
		if i <= 0 or j <= 0:
			curr = X[:i] + Y[:j] + curr
			ans.add(curr)
			return
		if X[i-1] == Y[j-1]:
			return helper(i-1,j-1,ans,X[i-1]+curr)
			
		else:
			if dp[i][j-1] <= dp[i-1][j]:
				helper(i,j-1,ans,Y[j-1]+curr)
			if dp[i-1][j] <= dp[i][j-1]:
				helper(i-1,j,ans,X[i-1]+curr)
		
	ans = set()
	helper(l1,l2,ans,"")
	return ans
	
# Implement diff utility in Python
if __name__ == '__main__':

	X = "ABCBDAB"
	Y = "BDCABA"


	# find the difference
	print(SCS_ALL(X, Y))
	print(SCS_By_LCS_ALL(X,Y))
	# print(SCS_Length(X, Y))
