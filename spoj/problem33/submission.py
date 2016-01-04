def fast_LCS_with_values(s1,s2):
  def fast_LCS_helper(s1,s2,memo):
    if (s1,s2) in memo:
      return memo[(s1,s2)]
    if (s1 == "" or s2 == ""):
      result = (0,[""])
    elif (s1[0] == s2[0]):
      lose_both = fast_LCS_helper(s1[1:],s2[1:],memo)
      result = ( 1+lose_both[0], [ s1[0]+s for s in lose_both[1] ] )
    else:
      uses1 = fast_LCS_helper(s1,s2[1:],memo)
      uses2 = fast_LCS_helper(s1[1:],s2,memo)
      if uses1[0] > uses2[0]:
        result = uses1
      elif uses1[0] < uses2[0]:
        result = uses2
      else:
        result = ( uses1[0] , list(set(uses1[1]+uses2[1])) )
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
	for s in srtd:
		print s
	print
	tests -= 1;