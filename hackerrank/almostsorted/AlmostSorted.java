/*
 *Daniel Vinakovsky, Vladislav Ligai, Mitchell Freedman
 *I pledge my honor that I have abided by the Stevens Honor System.
*/
import java.util.Scanner;
import java.util.Arrays;
import java.util.ArrayList;
import java.io.*;

public class AlmostSorted
{
    public static void solve(int[] nums)
    {
        //ArrayList to hold indices that were "swapped"//
        ArrayList<Integer> iswaps = new ArrayList<Integer>();
        int numswaps = 0;
        for (int i=0; i<nums.length-1; ++i)
            {
                if (nums[i] > nums[i+1])
                    {
			//record "swapped" index if there are less than 2 swaps total,
                        //or if we have repeating swaps (reverse case)
                        if (numswaps <= 1)
			    {
				++numswaps;
				iswaps.add((Integer)(i));
			    }
			else if (i-iswaps.get(iswaps.size()-1) == 1)
			    iswaps.add((Integer)(i));
                        //print no and exit early if conditions are no longer met
                        else
                            {
                                System.out.println("no");
                                System.exit(0);
                            }
                    }
            }
        //case that array is already sorted (0 swaps needed)
        if (numswaps == 0)
            {
                System.out.println("yes");
                System.exit(0);
            }
	//set variables while paying attn to 1-based indexing
	int iswaps_size = iswaps.size();
        int firstidx = iswaps.get(0);
        int lastidx  = iswaps.get(iswaps_size-1)+1;

	//case that we have a single swap
        if ( (firstidx == 0 || nums[lastidx] >= nums[firstidx-1]) && 
	     (lastidx == nums.length-1 || nums[firstidx] <= nums[lastidx+1]) &&
	     iswaps_size <= 2 )
            {
                System.out.println("yes");
                System.out.println("swap " + (firstidx+1) + " " + (lastidx+1));
            }
	//case that we have multiple, continuous swaps (reverse sub-array)
	else if ( (firstidx == 0 || nums[lastidx] >= nums[firstidx-1]) &&
		  (lastidx == nums.length-1 || nums[firstidx] <= nums[lastidx+1]) &&
		  iswaps_size > 2 )
            {
                System.out.println("yes");
                System.out.println("reverse " + (firstidx+1) + " " + (lastidx+1));
            }
        //no other cases for almost sorted array
        else
            System.out.println("no");

    }
    public static void main(String[] args)
    {
        /**************** input parsing *****************/
        Scanner in = new Scanner(System.in);
        int numIndices = Integer.parseInt(in.nextLine());
        String raw = in.nextLine();
        String[] sep = raw.split(" ");
        int[] nums = new int[sep.length];
        for (int i=0; i<sep.length; ++i)
            {
                nums[i] = Integer.parseInt(sep[i]);
            }
        /************************************************/
        //print solution
        solve(nums);

    }
}
