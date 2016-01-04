/*
 *Daniel Vinakovsky & Vladislav Ligai
 *I pledge my honor that I have abided by the Stevens Honor System.
 *Project Euler #4 Solution
*/

public class LargestPalindromeProduct
{
    //pre: checkrev(int checknum) takes an integer
    //post: returns true if it is palindrome
    public static boolean checkrev(int checknum)
    {
	int revnum = 0;
	int intcmp = checknum;
	//algorithm to reverse number (assembles number backwards)
	for (; checknum>0; checknum=checknum/10)
	    revnum = (checknum%10) + (10*revnum);
	//return true if the reversed number is equal to the original number.
	if (revnum == intcmp)
	    return true;
	return false;
    }
    public static void main(String[] args)
    {
	int palproduct = 0;
	int tmp = 0;
	//multiply numbers, but start from 999 for both i and j.
	//faster than starting from 100 and going up as we're looking for the
	//_LARGEST_ palindrome.
	for (int i=999; i>=100; --i)
	    for (int j=999; j>=i; --j)
		{
		    //store in variable to avoid having to multiply more than once.
		    tmp = i*j;
		    //break out of the inner for loop as there is no way that we can have a larger palindrome
		    //when counting downwards. we may have a larger one with a different 'i' value though, so 
		    //continue with outer.
		    if (tmp <= palproduct)
		    	break;
		    //reassign if greater and a palindrome.
		    if (checkrev(tmp) && tmp>palproduct)
			palproduct = tmp;
		}
	//print final answer to screen
	System.out.println(palproduct);
	return;
    }
}
