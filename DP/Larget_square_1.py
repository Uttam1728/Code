# Function to find the size of the largest square submatrix of 1's
# present in a given binary matrix
def findLargestSquare(matrix):
	if not matrix : return 0
	
	dp = [ [0]*len(matrix[0]) for _ in range(len(matrix))]
	ans = 0
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if i == 0 or j == 0:
				dp[i][j] = matrix[i][j]
			else:
				dp[i][j] =  min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j]) + 1 if matrix[i][j] == 1 else 0
		ans = max(ans,dp[i][j])
        
	return ans

if __name__ == '__main__':

	M = [
			[0, 0, 1, 0, 1, 1],
			[0, 1, 1, 1, 0, 0],
			[0, 0, 1, 1, 1, 1],
			[1, 1, 0, 1, 1, 1],
			[1, 1, 1, 1, 1, 1],
			[1, 1, 0, 1, 1, 1],
			[1, 0, 1, 1, 1, 1],
			[1, 1, 1, 0, 1, 1]
		]

	# `size` stores the size of the largest square submatrix of 1's
	maxsize = findLargestSquare(M)

	print("The size of the largest square submatrix of 1's is", maxsize)
