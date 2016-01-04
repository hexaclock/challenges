#Vladislav Ligai, Nicholas Massa, Daniel Vinakovsky
#I pledge my honor that I have abided by the Stevens Honor System.

def fast_LCS_with_values(s1,s2):
  def fast_LCS_helper(s1,s2,memo):
    #check if the tuple of s1 and s2 is memoized
    if (s1,s2) in memo:
      return memo[(s1,s2)]
    #base case
    if (s1 == "" or s2 == ""):
      result = (0,[""])
    #if the first letter of each string match
    elif (s1[0] == s2[0]):
      #record this is as a match (increment counter in result), and "lose both" to continue going through the rest of the strings
      lose_both = fast_LCS_helper(s1[1:],s2[1:],memo)
      #add match to all lists
      result = ( 1+lose_both[0], [ s1[0]+s for s in lose_both[1] ] )
    else:
      #call fast_LCS_helper with different use/lose cases
      uses1 = fast_LCS_helper(s1,s2[1:],memo)
      uses2 = fast_LCS_helper(s1[1:],s2,memo)
      #select value to return depending on the length of each string
      if uses1[0] > uses2[0]:
        result = uses1
      elif uses1[0] < uses2[0]:
        result = uses2
      else:
        #in the case that they are of equal length, merge the lists together
        result = ( uses1[0] , list(set(uses1[1]+uses2[1])) )
    #record return value in memo (dictionary)
	memo[(s1,s2)] = result
    return result
  return fast_LCS_helper(s1,s2,{})


#drive fast_LCS_with_values using SPOJ input
tests = int(raw_input())
str1 = ""
str2 = ""
while (tests > 0):
	str1 = str(raw_input())
	str2 = str(raw_input())
	srtd = sorted(fast_LCS_with_values(str1,str2)[1])
	#sort to satisfy spoj
	for s in srtd:
		print s
	print
	tests -= 1;