def solution():
	return sumDigits(str(2**1000))
	
def sumDigits(bignumstr):
	if bignumstr == '':
		return 0
	elif len(bignumstr)==1:
		return int(bignumstr[0])
	else:
		return int(bignumstr[0]) + sumDigits(bignumstr[1:])
		
print solution()
	