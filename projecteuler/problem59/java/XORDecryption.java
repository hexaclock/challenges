import java.util.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

class XORDecryption
{
    /*
     *pre: takes a key, and the ciphertext
     *post: performs a repeating-key xor decryption, returns the result
     */
    public static char[] xordecrypt(char[] key, char[] ctxt)
    {
	char[] decrypt = new char[ctxt.length];

	for (int i=0; i<ctxt.length; ++i)
	    decrypt[i] = (char)(ctxt[i] ^ key[i%key.length]);
	return decrypt;
    }
    /*
     *pre: takes a char array, and percentage english (A-Za-z) threshold
     *post: returns true or false based on whether the string meets the criteria and whether it is greater or less than threshold
     */
    public static boolean checkenglish(char[] chars, int threshold)
    {
	double divisor = (double)chars.length;
	int loopmax = chars.length;
	int lettercount;
	int i;

	for (lettercount=0,i=0; i<loopmax; ++i)
	    if ( (chars[i] >= 97 && chars[i] <= 122) || (chars[i] >= 65 && chars[i] <= 90) || (chars[i] == 32) )
		++lettercount;
	
	if  ( ((lettercount / divisor) * 100) > threshold )
	    return true;
	else
	    return false;
	
    }

    /*
     *pre: takes a char[] array of ascii values
     *post: returns the sum of all of the ascii vals of the individual chars
     */
    public static int addasciivals(char[] chars)
    {
	int sum = 0;
	for (int x=0; x<chars.length; ++x)
	    sum += (int)chars[x];
	return sum;
    }
    
    /*
     *driver, file reader, and file parser function
     */
    public static void main(String[] args)
    {
	String rawin = "";
	String rawconcat = "";
	char[] key = {'a','a','a'};
	char a;
	char b;
	char c;

	try
	    {
		File fh = new File("../cipher.txt");
		BufferedReader in = new BufferedReader(new FileReader(fh));
		while ( (rawin = in.readLine()) != null )
		    rawconcat += rawin;
		in.close();
		
	    }
	catch (IOException e)
	    {
		System.out.println("error reading file");
	    }

	List<String> enclist = Arrays.asList(rawconcat.split(","));
	String[] encarr = enclist.toArray(new String[enclist.size()]);
	char[] encchars = new char[encarr.length];
	char[] dec;
	
	for (int i = 0; i < encarr.length; ++i)
	    encchars[i] = (char)Integer.parseInt(encarr[i]);

	/*try all combinations of aaa - zzz*/
	for (a=95; a<123; ++a)
	    {
		key[0] = a;
		for (b=95; b<123; ++b)
		    {
			key[1] = b;
			for (c=95; c<123; ++c)
			    {
				key[2] = c;
				/*if found, print relevant stats on the decrypted text*/
				if ( checkenglish( xordecrypt(key,encchars), 95 ) )
				    {
					dec = xordecrypt(key,encchars);
					System.out.print("Key: ");
					System.out.println(String.valueOf(key));
					System.out.print("Sum of ASCII Values: ");
					System.out.println(addasciivals(dec));
					System.out.println(String.valueOf(dec));
				    }
			    }
			
		    }
	    }
	
    }
}
