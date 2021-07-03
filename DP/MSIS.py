def MSIS(A,dp = None):
	la = len(A)
	if not dp : dp = [i for i in A]
	
	for i in range(1,la):
		for j in range(i):
			if A[i] > A[j] :
				dp[i] = max(dp[i], dp[j] + A[i])
	print(A)
	print(dp)
	return max(dp)

def MSIS_All(A,dpSeq = None):
	la = len(A)
	if not dpSeq : dpSeq = [ [[],0]  for _ in A]
	dpSeq[0] = [[A[0]],A[0]]
	
	for i in range(1,la):
		for j in range(i):
			if A[i] > A[j] and dpSeq[j][1] > dpSeq[i][1]:
				dpSeq[i][0] = dpSeq[j][0].copy()
				dpSeq[i][1] = dpSeq[j][1]
		dpSeq[i][0].append(A[i])
		dpSeq[i][1] += A[i]	
			
	print(A)
	print(dpSeq)
	return max(dpSeq, key = lambda l : l[1])

if __name__ == '__main__':

	# A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11] #, 7, 15]
	
	A = [1, 101, 2, 3, 100, 4, 5]

	print("The length of the MSIS is", MSIS(A))

	print("The length of the MSIS is", MSIS_All(A))
