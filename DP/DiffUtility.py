# Function to display the differences between two strings


def LCSLengthBottamUp(X, Y,dp = None):
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

	
def DiffUtility(X,Y):
	l1, l2 = len(X), len(Y)
	dp = [[0]*(l2+1) for i in range(l1+1)]
	
	LCSLengthBottamUp(X,Y,dp)


	def helper(i,j,curr):
		
		if i <= 0 or j <= 0 :
			return curr
		
		if X[i-1] == Y[j-1]:
			return helper(i-1,j-1," " +X[i-1]+curr)
			
		if dp[i][j-1] >= dp[i-1][j]:
			return helper(i,j-1," +"+Y[j-1]+curr)
		else:
			return helper(i-1,j," -"+X[i-1]+curr)
		

	return helper(l1,l2,"")


# Implement diff utility in Python
if __name__ == '__main__':

	X = "ABCDFGHJQZ"
	Y = "ABCDEFGIJKRXYZ"


	# find the difference
	print(DiffUtility(X, Y))
