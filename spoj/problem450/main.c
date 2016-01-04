#include <stdio.h>

int main()
{
  unsigned int n;
  unsigned int k;
  unsigned int number;
  unsigned int count;
  scanf("%d %d", &n, &k);
  while (n > 0)
    {
      scanf("%d", &number);
      if (number % k == 0)
	++count;
      --n;
    }
  printf("%d",count);
  return 0;
}
