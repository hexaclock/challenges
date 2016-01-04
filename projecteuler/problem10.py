import time
def solution():
	i=2
	total = 0
	start_time = time.time()
	while i<2000000:
		if isPrime(i):
			total+=i
			i+=1
		else:
			i+=1
	end_time = time.time()
	print("Elapsed time was %g seconds" % (end_time - start_time))
	return total


	
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
	
def otherisPrime(num):
	if num < 2:
		return False
	if num == 2:
		return True
	if num%2 == 0:
		return False
	else:
		for div in range(3,int(((num**0.5))+1),2):
			if num % div == 0:
				return False
		return True
		
print solution()