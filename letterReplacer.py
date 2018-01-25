#!/usr/bin/python2.7
#Geoges Brantley
# Goal: Easy way to break mono-ciphers
import sys
import string
import random

def printLet(listLet):
    outString = ""
    for x in listLet:
        outString += x
    print outString

if __name__ == "__main__":
    allLetters = []
 
    # open file, read it
    try:
        with open(sys.argv[1],'r') as f:
            # opens by line
            for line in f:
                # By letter
                for x in line:
                    #only if letter is uppercase
                    if x.isupper():
                        # Add to list
                        allLetters.append(x)
    except:
        print "Error in opening the File"
        sys.exit(0)


    past = ""
    #WHILE LOOP (GO TILL DONE!)
    if len(sys.argv) == 2:
        while (True):
            print "\nCurrent string: "
            printLet(allLetters)
            print "\nPast Switches: "
            print past
            print "" 
            base = raw_input("Letter to Replace: ")
            replace = raw_input("Letter to put there instead: ")

            past += "\n" + base + "<->" + replace
            for x in range(0,len(allLetters)):
                if allLetters[x] == base:
                    allLetters[x] = '0' 
                if allLetters[x]  == replace:
                    allLetters[x] = base    
            for x in range(0,len(allLetters)):
                if allLetters[x] == '0':
                    allLetters[x] = replace.lower() 
    else:
        # Random replace Brute force
        trans = {}
        stop = 0
        while (True):
            dic = string.letters
            dic = dic[26:]
            dic = list(dic)
            rand = dic
            random.shuffle(rand)
            fic = string.letters
            fic = fic[26:]
            fic = list(fic)
            for x in range(0,26):
                trans[str(fic[x])] = str(rand[x])
            # SET TRANSLATIONS
            # F -> E
            hold = trans['F']
            trans['F'] = 'E'
            trans[hold] = 'F'
            # X-> T
            hold = trans['X']
            trans['X'] = 'T'
            trans[hold] = 'X'
            #J -> H
            hold = trans['J']
            trans['J'] = 'H'
            trans[hold] = 'J'
            
            print str(trans)
            # translate file
            for base,replace in trans.iteritems():
                for x in range(0,len(allLetters)):
                    if allLetters[x].upper() == base.upper():
                        allLetters[x] = '0' 
                    if allLetters[x].upper()  == replace.upper():
                        allLetters[x] = base.upper()    
                for x in range(0,len(allLetters)):
                    if allLetters[x] == '0':
                        allLetters[x] = replace.upper() 
            newStr = ''.join(allLetters)
            # Test New Thing
            if 'THERE' in newStr and 'WHERE' in newStr and 'ING' in newStr:
                print "\n\n" + newStr
                switches = ""
                for base,replace in trans.iteritems():
                   switches += base + "->" + replace + " , " 
                stop += 1
                if stop > 10:
                    break 
