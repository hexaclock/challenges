#include <stdio.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

unsigned int gl_cleanbytes;

/*
 *function to print a single character
*/
void my_char(char c)
{
  write(1,&c,1);
}

/*
 *function to print a null-terminated string (char *)
*/
void my_str(char *s)
{
  if (s != NULL)
    for(; *s!='\0'; ++s)
      my_char(*s);
}

/*
 *pre: takes a key, ciphertext, and the number of bytes in the ciphertext
 *post: performs a repeating-key xor decryption, returns the result
*/
char *xordecrypt(char *key, unsigned int nbytes, char *ctxt)
{
  unsigned int i;
  unsigned int keylen;
  char *decrypt = (char *)malloc((nbytes+1)*sizeof(char));
  keylen = strlen(key);

  for (i=0; i<nbytes; ++i)
    decrypt[i] = ctxt[i] ^ key[i%keylen];
  decrypt[nbytes] = '\0';
  return decrypt; 
} 

/*
 *pre: takes a string (char *), percentage english (A-Za-z) threshold, and the number of bytes in the string.
 *post: returns 1 (true) or 0 based on whether the string meets the criteria and whether it is greater or less than threshold
*/
char checkenglish(char *asciilist, unsigned int threshold, unsigned int nbytes)
{
  unsigned int divisor = nbytes;
  unsigned int loopmax = nbytes;
  unsigned int lettercount;
  unsigned int i;
  
  for (lettercount=0,i=0; i<loopmax; ++i)
    if ( (asciilist[i] >= 97 && asciilist[i] <= 122) || (asciilist[i] >= 65 && asciilist[i] <= 90) || (asciilist[i] == 32) )
      ++lettercount;

  if ( ( (lettercount / (double)(divisor)) * 100) > threshold )
    return 1;
  else
    return 0;
}

/*
 *pre: takes a char * with commas separating numbers, and the size (bytes) of the char *
 *post: returns a clean char* without any commas (commas in *csv signify where to start a new index)
*/
char *parsecsv(char *csv, unsigned int nbytes)
{
  char *ret = (char *)malloc((nbytes+1)*sizeof(char));
  unsigned int i;
  unsigned int j;
  unsigned int cleancount;
  cleancount = 0;
  
  for (i=0; i<nbytes; i++)
    {
      ret[cleancount] = 0;
      j = 0;
      if (csv[i] != ',')
	{
	  for (j=i; csv[j] != ','; j++)
	    {
	      if (csv[j] >= '0' && csv[j]<='9')
		{
		  ret[cleancount] = 10*ret[cleancount];
		  ret[cleancount] += (csv[j]-48);
		}
	      else
		break;
	    }
	  ++cleancount;
	  i = j;
	}
    }
  gl_cleanbytes = cleancount;
  return ret;
}

/*
 *pre: takes a null-terminated string (char*)
 *post: returns the sum of all of the ascii vals of the individual chars up to the first '\0'
*/
unsigned int addasciivals(char *s)
{
  unsigned int sum;
  for (sum=0; *s != '\0'; ++s)
    sum += *s;
  return sum;
}

/*
 *driver and file reader function
*/
int main()
{
  FILE *file = fopen("../cipher.txt", "r");
  int n = 0;
  int c;
  char i;
  char j;
  char k;
  char *inputcsv = (char *)malloc(4096*sizeof(char));
  char *cleanctxt;
  char *key = (char *)malloc(4*sizeof(char));
  char *dec;
  
  while ((c = fgetc(file)) != EOF)
    inputcsv[n++] = (char)c;
  if (n<0)
    exit(1);
  fclose(file);

  cleanctxt = parsecsv(inputcsv,n);
  
  key[3] = '\0';

  /*try all combinations of aaa - zzz*/
  for (i=95; i<123; ++i)
    {
      key[0] = i;
      for (j=95; j<123; ++j)
	{
	  key[1] = j;
	  for (k=95; k<123; ++k)
	    {
	      key[2] = k;
	      /*if found, print relevant stats on the decrypted text*/
	      if ( checkenglish(xordecrypt(key,gl_cleanbytes-1,cleanctxt), 95, gl_cleanbytes) )
		{
		  dec = xordecrypt(key,gl_cleanbytes,cleanctxt);
		  my_str("Key: "); my_str(key); my_char('\n');
		  my_str("Sum of ASCII Values: "); printf("%d\n",(addasciivals(dec)));
		  my_str(dec); my_char('\n');
		  return 0;
		}
	    }
	}
    }
  return 1;
}
