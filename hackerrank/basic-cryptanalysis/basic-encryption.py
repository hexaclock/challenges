#https://www.hackerrank.com/challenges/basic-cryptanalysis
#updated: April 18, 2015 10:45PM EST#
#50/50 on HackerRank!#

PRESENTATION = False
DICTFILE     = 'dictionary.lst'

#length:dictwords list
DictWords = {}
#length:encwords list
EncWords = {}
#ctxt char:sub char
DoneSubs = {}
#Original String
rawcipher = ''

def parseDict():
    '''Read in dictionary.lst into DictWords'''
    fh = open(DICTFILE)
    for line in fh:
        val = line.split()
        val = ''.join(val)
        key = len(val)
        if key in DictWords:
            DictWords[key].append(val)
        else:
            DictWords[key] = [val]
    fh.close()
        
def parseInput():
    '''Read input ciphertext into EncWords'''
    global rawcipher
    enclist = raw_input().split(' ')
    maxlen  = 0
    for encword in enclist:
        key = len(encword)
        rawcipher += encword + " "
        if key in EncWords:
            EncWords[key].append(encword)
        else:
            EncWords[key] = [encword]
        if key > maxlen:
            maxlen = key
    return maxlen

def getEncWordsOfLength(l):
    '''Returns list of encrypted words of length l'''
    if l in EncWords:
        return EncWords[l]
    else:
        return []
            
def getDictWordsOfLength(l):
    '''Returns list of dictionary words of length l'''
    if l in DictWords:
        return DictWords[l]
    else:
        return []

def patternsMatch(str1,str2):
    '''Returns true if str1 and str2 have the same pattern,
    false otherwise.'''
    str1len  = len(str1)
    str2len  = len(str2)
    repcnt   = 0
    #dictionaries are awesome!
    workdict = {}
    if (str1len != str2len):
        return False
    for c in range(str1len):
        c1 = str1[c]
        c2 = str2[c]
        #we haven't seen this letter in str1 yet
        if (c1 not in workdict):
            #but it's already matched to some other letter
            if (c2 in workdict.values()):
                return False
            #or it's not matched yet, just match it up
            else:
                workdict[c1] = c2
        #we saw the letter from str1 before, but the current c2 doesn't match the 
        #previously established pattern
        elif (workdict[c1] != c2):
            return False
        elif (workdict[c1] == c2):
            repcnt+=1
    #they follow the same pattern if we reach here
    #but we need to tune for our problem
    if str1len < 5 and repcnt >= 3:
        return True
    if str1len < 10 and repcnt >= 2:
        return True
    if str1len >= 10 and repcnt >= 1:
        return True
    return False

def addPatternSubs(enclen):
    '''Automatically adds ctxt char->ptxt char mappings to DoneSubs
    based on if the ptxt word and the ctxt word follow the same pattern'''
    pwords = getDictWordsOfLength(enclen)
    cwords = getEncWordsOfLength(enclen)
    ptxtchars = DoneSubs.values()
    for cword in cwords:
        for pword in pwords:
            if patternsMatch(cword,pword):
                #create mapping
                for c in range(enclen):
                    #never overwrite a previous (higher probability) mapping
                    if cword[c] not in DoneSubs and pword[c] not in ptxtchars:
                        DoneSubs[cword[c]] = pword[c]

def getWordsAsList():
    '''Returns all words in their current state (with mappings) as a list
    If a mapping for a character in a given word does not yet exist, 
    a ? is prefixed to the character'''
    global rawcipher
    ret = []
    tempstr = ''
    for c in rawcipher:
        if c in DoneSubs and DoneSubs[c] != '' and DoneSubs[c] != ' ':
            tempstr += DoneSubs[c]
        elif c in DoneSubs and DoneSubs[c] == ' ':
            ret.append(tempstr)
            tempstr = ''
        else:
            tempstr += '?'+c
    return ret
    
def getUnfinished():
    '''Returns list of words that have not been fully cracked yet'''
    #a ? before a character in word means that char still needs a mapping
    return filter(lambda word: "?" in word, getWordsAsList())
    
def charRepeats(str1,c):
    '''Checks if a character repeats (more than 1 occurrence'''
    repeat = 0
    for ltr in str1:
        if repeat > 1:
            return True
        elif ltr == c:
            repeat += 1
    return False
    
def getAlmostDecr():
    '''Returns a list of words with a single unmapped character'''
    unfin = getUnfinished()
    almost = []
    workdict = {}
    for word in unfin:
        if not charRepeats(word,'?'):
            almost.append(word)
    return almost
    
def getReplaceIndex(cword,repl):
    '''Checks if a word with an unmapped character can be located in the dictionary
    given a "try" character "repl"'''
    words = getDictWordsOfLength(len(cword)-1)
    lcword = list(cword)
    cwlen = len(cword)
    for i in range(cwlen):
        lcword = list(cword)
        if lcword[i] == '?':
            del lcword[i]
            lcword[i] = repl
            if ''.join(lcword) in words:
                return i+1
    return -1
    
def tryFinishUp():
    '''Perform a simplified brute force against words with unmapped characters,
    create mapping in DoneSubs if the word ends up existing in the dictionary.'''
    alreadydone = DoneSubs.values()
    remain = []
    almostdecr = getAlmostDecr()
    for C in range(ord('A'),ord('Z')+1):
        remain.append(chr(C))
    for c in range(ord('a'),ord('z')+1):
        remain.append(chr(c))
    for c in remain:
        if c in alreadydone:
            remain.remove(c)
    for cword in almostdecr:
        for sb in remain:
            idx = getReplaceIndex(cword,sb)
            if idx != -1:
                DoneSubs[cword[idx]] = sb
                
def substituteWords():
    '''Prints solution / decrypted ciphertext'''
    global rawcipher
    output = ''
    for c in rawcipher:
        if c in DoneSubs and DoneSubs[c] != '':
            output += DoneSubs[c]
        else:
            output += c
    return output

def main():
    global rawcipher
    parseDict()
    encmax = parseInput()
    #allows for easy printing of solution
    DoneSubs[' '] = ' '
    #create mappings starting with longest words first
    #7 is kind of a magic number
    lowerbound = 7
    for i in range(encmax,lowerbound,-1):
        addPatternSubs(i)
    if PRESENTATION:
        print ""
        print "We have " + str(len(DoneSubs)-1) + " mappings before simplified brute force."
    #try to brute force remaining unsolved words
    tryFinishUp()
    if PRESENTATION:
        print "We have " + str(len(DoneSubs)-1) + " mappings after simplified brute force."
        print ""
    #print the output
    print substituteWords()
    if PRESENTATION:
        print ""
        print "The key:"
        print ''.join(DoneSubs.keys())
        print ''.join(DoneSubs.values())
    
main()
