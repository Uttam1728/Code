import sys


# Function to find the length of the longest increasing subsequence
def LIS_Length(A):
	dp = [1]*(len(A))
	for i in range(1,len(A)):
		for j in range(i):
			if A[j] < A[i]:
				dp[i] = max(dp[i],1+dp[j])
	print(dp)
	return max(dp)

def LIS_ByDPTable(A):
	dp = [1]*(len(A))
	dpSeq = [[] for i in range(len(A))]
	dpSeq[0] = [A[0]]
	
	for i in range(1,len(A)):
		curr = A[i]
		currSeq = []
		
		for j in range(i):
			if curr > A[j] and (1+dp[j]) > dp[i] :
				dp[i] = 1+dp[j]
				currSeq = dpSeq[j].copy()
				
		currSeq.append(curr)
		dpSeq[i] = currSeq
		
	for i in range(len(dpSeq)):
		print(i,"|",A[i],"|",dpSeq[i])

	return max(dpSeq,key = len)

def LIS(A):
	dpSeq = [[] for i in range(len(A))]
	dpSeq[0] = [A[0]]
	
	for i in range(1,len(A)):
		curr = A[i]

		for j in range(i):
			if curr > A[j] and len(dpSeq[j]) > len(dpSeq[i]) :
				dpSeq[i] = dpSeq[j].copy()
				
		dpSeq[i].append(curr)

	for i in range(len(dpSeq)):
		print(i,"|",A[i],"|",dpSeq[i])

	return max(dpSeq,key = len)



if __name__ == '__main__':

	A = [0, 8, 4, 12, 2,2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

	print("The length of the LIS is", LIS_Length(A))

	print("The length of the LIS is", LIS(A))

	print("The length of the LIS is", LIS_ByDPTable(A))
