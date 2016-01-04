#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <unistd.h>

#define PRSNT 0

/*
 *returns a 5001x5001 2D "array"
*/
int **mallocdparr()
{
  int **dparr;
  int i;
  dparr = (int **)malloc(5001*sizeof(int *));

  for (i=0; i<5001; ++i)
    dparr[i] = (int *)calloc(5001,sizeof(int));

  return dparr;
}

int main()
{
  char *strnga;
  char *strngb;
  char c;
  int  **dp;
  int  x;
  int  y;
  int  i;
  int  j;
  /* turn off printf buffering */
  setvbuf(stdout, NULL, _IONBF, 0);
  dp = mallocdparr();
  /* malloc strings, and parse input */
  strnga = (char *)malloc(5001*sizeof(char));
  strngb = (char *)malloc(5001*sizeof(char));
  for (x=0; (((c=getchar())!=0) && c!='\n') ;x++)
    strnga[x] = c;
  for (y=0,c=0; (((c=getchar())!=0) && c!=EOF && c!='\n') ;y++)
    strngb[y] = c;

  /* bounds start at 1 to simplify code/less if statements */
  for (i=1; i<=x; ++i)
    {
      for (j=1; j<=y; ++j)
        {
	  /* we have a match, just store val from prev pass + 1 */
          if (strnga[i-1] == strngb[j-1])
            dp[i][j] = dp[i-1][j-1]+1;
	  /* copy value from previous pass */
          else if (dp[i-1][j] >= dp[i][j-1])
            dp[i][j] = dp[i-1][j];
	  /* copy value from last iteration */
          else
            dp[i][j] = dp[i][j-1];
        }
    }
  
  if (PRSNT)
    {
      /* print dp array */
      for (i=0;i<=x;++i)
	{
	  for (j=0;j<=y;++j)
	    printf("%d%s",dp[i][j],",");
	  puts("");
	}
    }
  /* answer is in the last box */
  printf("%d",(int)dp[x][y]);
  return 0;
}
