def solution(number):
	i=2 #start divisor at 2
	maxprime = 0 #variable that will keep track of maxprime
	while number!=1: #while we have not divided number to 1
		if number%i==0 and isPrime(i) and i>maxprime: #if the number is divisible by the divisor, the divisor is prime, and the divisor is greater than the greatest prime factor we've seen so far
			maxprime = i #set maxprime equal to our divisor
			number = number/i #divide the number by the divisor
			i=2 #reset the divisor back to 2
		else:
			i+=1 #otherwise, keep incrementing the divisor in hopes of getting a clean division at the start of the next loop iteration
	return maxprime
	
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
	
print solution(600851475143)