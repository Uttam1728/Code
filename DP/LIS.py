import sys


# Function to find the length of the longest increasing subsequence
def LIS(A):
	dp = [1]*(len(A))
	for i in range(1,len(A)):
		for j in range(i):
			if A[j] < A[i]:
				dp[i] = max(dp[i],1+dp[j])
	print(dp)
	return dp[-1]



if __name__ == '__main__':

	A = [0, 8, 4, 12, 2,2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

	print("The length of the LIS is", LIS(A))
