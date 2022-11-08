#Natasha Needham
#Longest Common Subsequence Problem



import time
import string
import random
# Dynamic Programming implementation of LCS problem 
def dynamic_LCS(X , Y): 
	m = len(X) 
	n = len(Y) 
  
	L = [[None]*(n+1) for i in range(m+1)] 
  
	for i in range(m+1): 
		for j in range(n+1): 
			if i == 0 or j == 0 : 
				L[i][j] = 0
			elif X[i-1] == Y[j-1]: 
				L[i][j] = L[i-1][j-1]+1
			else: 
				L[i][j] = max(L[i-1][j] , L[i][j-1]) 
	#the following prints the LCS itself
	index = L[m][n] 
  
	lcs = [""] * (index+1) 
	lcs[index] = "" 
  
	
	i = m 
	j = n 
	while i > 0 and j > 0: 
  
		if X[i-1] == Y[j-1]: 
			lcs[index-1] = X[i-1] 
			i-=1
			j-=1
			index-=1
  
		elif L[i-1][j] > L[i][j-1]: 
			i-=1
		else: 
			j-=1
  
	print ("LCS of " + X + " and " + Y + " is " + "".join(lcs))
  
	return L[m][n] 
 

#Brute force algorithm 
def brute_force_LCS(X, Y, m, n): 
	if m == 0 or n == 0: 
		return 0
	elif X[m-1] == Y[n-1]: 
		return 1 + brute_force_LCS(X, Y, m-1, n-1)
	else: 
		return max(brute_force_LCS(X, Y, m, n-1), brute_force_LCS(X, Y, m-1, n))
	
 
if __name__ == "__main__":
	x = ''.join(random.choices(string.ascii_uppercase, k = 10)) #random cases
	Y = ''.join(random.choices(string.ascii_uppercase, k = 10)) #random cases
	#Y = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	#x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #best case
	#x = "QRSTUVWXYZ" #worst case
	#Y = "ABCDEFGHIJ" #worst case
	tic = time.perf_counter()
	print ("Length of LCS is ", brute_force_LCS(x, Y, len(x), len(Y)))
	toc = time.perf_counter()
	print("LCS found with dynamic algorithm:")
	tic1 = time.perf_counter()
	dynamic_LCS(x, Y)
	toc1 = time.perf_counter()

	print(f"Brute force algorithm took {10*(toc-tic):0.4f} seconds")
	print(f"Dynamic algorithm took {1000*(toc1-tic1):0.4f} seconds")
