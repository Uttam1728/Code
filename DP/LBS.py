import sys


# Function to find the length of the longest increasing subsequence
def LIS_Length(A,dp = None):
	if not dp : dp = [1]*(len(A))
	for i in range(1,len(A)):
		for j in range(i):
			if A[j] < A[i]:
				dp[i] = max(dp[i],1+dp[j])
	print(dp)
	return max(dp)
	
def LDS_Length(A,dp = None):
	if not dp : dp = [1]*(len(A))
	for i in range(len(A)-1,-1,-1):
		for j in range(len(A)-1,i,-1):
			if A[j] < A[i]:
				dp[i] = max(dp[i],1+dp[j])
	print(dp)
	return max(dp)
	
def LBS_Length(A):
	lis = [1]*(len(A))
	lds = [1]*(len(A))
	LIS_Length(A,lis)
	LDS_Length(A,lds)
	ans = 0
	for i,j in zip(lis,lds):
		ans = max(ans,i+j-1)
	return ans

def LIS(A,dpSeq = None):
	if not dpSeq :  dpSeq = [[] for i in range(len(A))]
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
	
def LDS(A,dpSeq = None):
	if not dpSeq : [[] for i in range(len(A))]
	dpSeq[-1] = [A[-1]]
	
	for i in range(len(A)-2,-1,-1):
		curr = A[i]

		for j in range(len(A)-1,i,-1):
			if curr > A[j] and len(dpSeq[j]) > len(dpSeq[i]) :
				dpSeq[i] = dpSeq[j].copy()
				
		dpSeq[i] = [curr] + dpSeq[i]

	for i in range(len(dpSeq)):
		print(i,"|",A[i],"|",dpSeq[i])

	return max(dpSeq,key = len)
	
def LBS(A):
	dpSeqLIS = [[] for i in range(len(A))]
	dpSeqLDS = [[] for i in range(len(A))]
	LIS(A,dpSeqLIS)
	LDS(A,dpSeqLDS)
	ansIndex  = 0
	
	for i in range(len(A)):
		if len(dpSeqLIS[i]) + len(dpSeqLDS[i]) - 1 > ansIndex:
			ansIndex = i
	return dpSeqLIS[ansIndex] + dpSeqLDS[ansIndex] 

if __name__ == '__main__':

	A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
	
	# A = [4, 2, 5, 9, 7, 6, 10, 3, 1]

	print("The length of the LbS is", LBS(A))
