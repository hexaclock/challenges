def fast_LCS_with_values(s1,s2):
  def fast_LCS_helper(s1,s2,memo):
    if (s1,s2) in memo:
      return memo[(s1,s2)]
    if (s1 == "" or s2 == ""):
      result = (0,[])
    elif (s1[0] == s2[0]):
      lose_both = fast_LCS_helper(s1[1:],s2[1:],memo)
      #add letter to all in list
      result = (1+lose_both[0], [s1[0]]+[lose_both[1]])
    else:
      uses1 = fast_LCS_helper(s1,s2[1:],memo)
      uses2 = fast_LCS_helper(s1[1:],s2,memo)
      if uses1[0] > uses2[0]:
        result = uses1
      elif uses1[0] < uses2[0]:
        result = uses2
      else:
        mergedstr = listmerge(uses1,uses2)[1]
        result = (mergedstr,mergedstr,memo)
    memo[(s1,s2)] = result
    print result
    return result
  return fast_LCS_helper(s1,s2,{})
  

  
def listmerge(lst1,lst2):
	len1 = len(lst1[1])
	len2 = len(lst2[1])
	mergedlist = ""

	for i in range(len1):
		if (lst1[1][i] not in mergedlist):
			mergedlist += lst1[1][i]
		if (lst2[1][i] not in mergedlist):
			mergedlist += lst2[1][i]
	return (len(mergedlist),mergedlist)

print fast_LCS_with_values("abcabcaa","acbacba")
