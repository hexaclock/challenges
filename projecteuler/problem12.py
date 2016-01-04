def solution():
	x=1
	i=2
	while numDivisors(x)<501:
		x = x+i
		i+=1
	return x
		

def numDivisors(number):
	i=2
	divisors = [1,number] #array that will keep track of divisors
	while i<((number**0.5)+1):
		if number%i==0:
			divisors += [i]
			divisors += [number/i]
			i+=1
		else:
			i+=1
	return len(divisors)
	
print solution()