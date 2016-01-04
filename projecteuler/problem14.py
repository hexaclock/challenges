def solution():
	longestseq = []
	for i in range(2,1000000):
		seq = []
		x=i
		while x>0:
			if x==1:
				seq+=[x]
				if len(seq)>len(longestseq):
					longestseq=seq
				x=-1
			elif isEven(x):
				x=(x/2)
				seq+=[x]
				if len(seq)>len(longestseq):
					longestseq=seq
			elif isEven(x)==False:
				x=((3*x)+1)
				seq+=[x]
				if len(seq)>len(longestseq):
					longestseq=seq
	print longestseq[0]

def isEven(n):
	if n%2==0:
		return True
	else:
		return False
		
solution()