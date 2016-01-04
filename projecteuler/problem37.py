def solution():
	truncPrimes = []
	num = 10
	while (len(truncPrimes)!=11):
		if isPrime(num):
			if isTruncPrime(str(num)):
				truncPrimes += [num]
		num+=1
	print sum(truncPrimes)
		
		
def isTruncPrime(primenumstr):
	if (isPrimeLeft(primenumstr) and isPrimeRight(primenumstr)):
		return True
	else:
		return False
	
def isPrimeLeft(primenumstr):
	if primenumstr=='':
		return True
	else:
		if isPrime(int(primenumstr)):
			return isPrimeLeft(primenumstr[1:])
		else:
			return False	
		
def isPrimeRight(primenumstr):
	if primenumstr=='':
		return True
	else:
		if isPrime(int(primenumstr)):
			return isPrimeRight(primenumstr[:-1])
		else:
			return False

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
	
solution()