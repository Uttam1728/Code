def Levenshtein_dist_Mem(X,Y):
	lx, ly = len(X), len(Y)
	cache = {}
	def helper(i,j):
		key = (i,j)
		if key not in cache:
			# print(i,j)
			if i == 0 or j == 0:
				cache[key] =  i + j
			elif X[i-1] == Y[j-1]:
				cache[key] = helper(i-1,j-1)
			else : 
				cache[key] = 1 + min(helper(i-1,j-1), helper(i,j-1), helper(i-1,j))
		
		return cache[key]

	return helper(lx,ly)
	
def Levenshtein_dist_DP(X,Y,dp = None):
	lx, ly = len(X), len(Y)
	if not dp: 
		dp = [[0]*(ly+1) for _ in range(lx+1)]
	
	for i in range(lx+1):
		for j in range(ly+1):
			if i == 0 or j == 0:
				dp[i][j] = i + j
			elif X[i-1] ==Y[i-1]:
				dp[i][j] = dp[i-1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
	

	return dp[lx][ly]

if __name__ == '__main__':
	X = "kitten"
	Y = "sitting"
	
	print("The Levenshtein distance is", Levenshtein_dist_Mem(X,Y))
	
	print("The Levenshtein distance is", Levenshtein_dist_DP(X,Y))
