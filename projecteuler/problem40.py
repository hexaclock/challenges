def solution():
	numstr = ''
	for i in range(1,1000001):
		numstr += str(i)
	answer = int(numstr[0])*int(numstr[9])*int(numstr[99])*int(numstr[999])*int(numstr[9999])*int(numstr[99999])*int(numstr[999999])
	return answer
	
print solution()