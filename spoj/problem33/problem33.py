def LCS(s1,s2):
  if (s1 == "" or s2 == ""):
    return 0
  if (s1[0] == s2[0]):
    return 1 + LCS(s1[1:],s2[1:])
  else:
    return max(LCS(s1[0:],s2[1:]),LCS(s1[1:],s2[0:]))

def LCS_with_values(s1,s2):
  if (s1 == "" or s2 == ""):
    return [0, ""]
  if (s1[0] == s2[0]):
    result = LCS_with_values(s1[1:],s2[1:])
    return [1+result[0], (s1[0] + result[1])]
  else:
    uses1 = LCS_with_values(s1,s2[1:]);
    uses2 = LCS_with_values(s1[1:],s2);
    if uses1[0] > uses2[0]:
      print uses1
      return uses1
    else:
      print uses2
      return uses2

def fast_LCS_helper(s1,s2,memo):
	if (s1,s2) in memo:
		return memo[(s1,s2)]
	if (s1 == "" or s2 == ""):
		result = (0,[])
	elif (s1[0] == s2[0]):
		lose_both = fast_LCS_helper(s1[1:],s2[1:],memo)
		result = ( 1+lose_both[0] , [s1[0]]+lose_both[1] )
	else:
		uses1 = fast_LCS_helper(s1,s2[1:],memo)
		uses2 = fast_LCS_helper(s1[1:],s2,memo)
		if uses1[0] > uses2[0]:
			result = uses1
		elif uses1[0] < uses2[0]:
			result = uses2
		else:
			result = uses1 + uses2
	memo[(s1,s2)] = result
	return result

def fast_LCS_with_values(s1,s2):
	return fast_LCS_helper(s1,s2,{})
  
def addelemtoall(elem,multlist):
	print multlist
	for lst in multlist:
		print elem
		lst.append(elem)
	return multlist
  
def listmerge(lst1,lst2):
	#len1 = len(lst1[1])
	#len2 = len(lst2[1])
	mergedlist = [lst1,lst2]
	return mergedlist
	#for i in range(len1):
	#	if (lst1[1][i] not in mergedlist):
	#		mergedlist += lst1[1][i]
	#	if (lst2[1][i] not in mergedlist):
	#		mergedlist += lst2[1][i]
	#print mergedlist
	#return mergedlist

print fast_LCS_with_values("abcabcaa","acbacba")
