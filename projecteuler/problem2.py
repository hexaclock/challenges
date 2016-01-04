memo={}
count = 0
def fastFib(N):
		if N==0 or N==1:
				return N
		elif memo.has_key(N):
				return memo[N]
		else:
				fibber = (fastFib(N-1) + fastFib(N-2))
				if fibber%2==0:
					global count
					count = count+fibber
				memo[N] = fibber
				return fibber
				
print fastFib(33)
print count