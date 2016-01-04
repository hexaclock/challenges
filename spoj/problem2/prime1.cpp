#include <iostream>
#include <stdio.h>
#include <cmath>
	
void sieve(unsigned int limit_, bool *is_prime_) 
{
  // the primes sieve algorithm
  if (limit_ > 0)
    is_prime_[0] = false;
  
  if (limit_ > 1)
    is_prime_[1] = false;
  
  for (unsigned int i=2; i<=limit_; ++i)
    is_prime_[i] = true;
  
  for (unsigned int i=2, i_bound=(int)sqrt(limit_); i<=i_bound; ++i)
    if (is_prime_[i] == true)
      for (unsigned int j=(i*i); j<=limit_; j+=i)
	is_prime_[j] = false;
}

int main(int argc, char *argv[])
{
  
  int cases;
  scanf("%d",&cases);
  unsigned int a; //low
  unsigned int b; //high
  unsigned int sb;
  int i;

  while (cases > 0)
    {
      scanf("%d %d", &a, &b);
      
      sb = sqrt(b);
      
      bool low_primes[sb];
      bool high_primes[b-a+1];
      
      //sieve on low_primes up to sqrt(b)//
      sieve(sb,low_primes);
      
      //set all high primes to true.//
      for(unsigned int x=0; x<=b-a+1; ++x)
	high_primes[x] = true;
      
      for (unsigned int p=2; p<=sb; ++p)
	if (low_primes[p] == true)
	  for (i = (unsigned int)ceil(a/(float)p); i*p<=b; ++i)
	      if ((int)(i*p-a) >= 0)
		high_primes[i*p-a] = false;

      //print any low primes starting from a//
      for (unsigned int k=a; k<=sb; ++k)
	if (low_primes[k] == true)
	  std::cout<<k<<std::endl;
      
      //print all high primes//
      for (unsigned int j=0; j<(b-a+1); ++j)
	if (high_primes[j] == true && j+a != 1)
	  std::cout<<j+a<<std::endl;
      
      //ensure no trailing line break after program completes//
      if (cases-1 != 0)
	std::cout<<std::endl;
      
      --cases;
    }
  return 0;
}
