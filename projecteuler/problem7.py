def solution():
	count = 0
	i = 1
	primenum = 0
	while count<10002:
		if isPrime(i):
			primenum = i
			count += 1
	return primenum
	
def isPrime(number):
	#Rudimentary sieve
	if number<2:
		return False
	if number == 2:
		return True
	if number%2==0:
		return False
	#Full check
	i = 3
	while i<(int(number**0.5)+1):
		if number%i==0:
			return False
		i+=2
	return True
	
print solution()