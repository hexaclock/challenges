def solution():
	maxpal = 0
	for i in range(100,1000):
		for j in range(100,1000):
			if (i*j)>maxpal:
				if str(i*j)==reverse(str(i*j)):
					maxpal = (i*j)
	return maxpal
	
def reverse(S):
        if (S==''):
                return S
        else:
                return reverse(S[1:]) + S[0]
				
print solution()