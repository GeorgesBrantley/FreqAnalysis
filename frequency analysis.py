#!/usr/bin/python2.7
# Georges Brantley
# PS02, HW 8
import sys


if __name__ == "__main__":
    # list of all letters, caps, in order that they appear
    allLetters = []

    # SEE IF THERE ARE ARGS
    if len(sys.argv) <= 1:
        print 'No file selected!'
        print 'Run \'./frequency analysis.py   filename\''
        sys.exit(0)
    
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

    # Doubles and Triples!
    singles = {}
    doubles = {}
    triples = {}
    nex = 0 # next word in list
    tri = 1 # word two ahead 

    #Traverse the List
    for a in allLetters:
        # nex is the next letter
        nex += 1
        tri += 1

        # Finding Singles!
        if a in singles:
            # Add value if found
            singles[a] += 1
        else:
            # add key to dictionary
            singles[a] = 1

        # Finding Doubles!
        # stop before going out of bounds
        if nex < len(allLetters):
            # get Letter Pair
            pair = a + allLetters[nex]

            # Check dictionary
            if pair in doubles:
                doubles[pair] += 1
            else:
                doubles[pair] = 1

        # Finding Triples!
        # stop before out of bounds
        if tri < len(allLetters):
            trip = a + allLetters[nex] + allLetters[tri]
        
            # check dictionary
            if trip in triples:
                triples[trip] += 1
            else:
                triples[trip] = 1 
    
    # Put dictionary into a sorted array based on value (reverse)
    z = sorted(singles, key=lambda key: singles[key])
    x = sorted(doubles, key=lambda key: doubles[key])
    y = sorted(triples, key=lambda key: triples[key])

    # iterate through top ten, show them!
    ten = 0
    # SHOWS SINGLES!
    print "Single Freq:"
    for let in reversed(z):
        if ten == 10:
            break
        print let + ": " + str(singles[let])
        ten += 1

    ten = 0
    # iterate through top ten, show them!
    # SHOWS Doubles!
    print "\nPair Freq:"
    for let in reversed(x):
        if ten == 10:
            break
        print let + ": " + str(doubles[let])
        ten += 1

    ten = 0
    # iterate through top ten, show them!
    # SHOWS Triples!
    print "\nTriplets Freq:"
    for let in reversed(y):
        if ten == 10:
            break
        print let + ": " + str(triples[let])
        ten += 1

