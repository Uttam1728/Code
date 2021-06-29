import sys


# Function to find the length of the longest Decreasing subsequence
def LDS(A):
	dpSeq = [[] for i in range(len(A))]
	dpSeq[0] = [A[0]]
 
	for i in range(1,len(A)):
		curr = A[i]

		for j in range(i):
			if curr < A[j] and len(dpSeq[j]) > len(dpSeq[i]) :
				dpSeq[i] = dpSeq[j].copy()
				
		dpSeq[i].append(curr)

	for i in range(len(dpSeq)):
		print(i,"|",A[i],"|",dpSeq[i])

	return max(dpSeq,key = len)


if __name__ == '__main__':

	A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

	print("The length of the LDS is", LDS(A))
