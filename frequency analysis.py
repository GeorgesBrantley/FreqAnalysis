#!/usr/bin/python2.7
# Georges Brantley
# PS02, HW 8
import sys


if __name__ == "__main__":
    # list of all letters, caps, in order that they appear
    allLetters = []

    # TODO accept standard in
    data = sys.stdin.readlines()
    print data

    # SEE IF THERE ARE ARGS
    #if len(sys.argv) <= 1:
    #    print 'No file selected!'
    #    print 'Run \'./frequency analysis.py   filename\''
    #    sys.exit(0)
    
    # opens by line
    for line in data:
        for let in line:
            # By letter
            for x in line:
                #only if letter is uppercase
                if x.isupper():
                    # Add to list
                    allLetters.append(x)
                # Makes lowercase uppercase now
                elif x.islower():
                    allLetters.append(x.upper())

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
    # fix it so its big to small
    z = reversed(z)
    x = reversed(x)
    y = reversed(y)
    
    # Do top Ten if there is an argment
    if len(sys.argv) > 2:
        if sys.argv[2] == '-ten':
            # iterate through top ten, show them!
            ten = 0
            # SHOWS SINGLES!
            print "Single Freq:"
            for let in z:
                if ten == 10:
                    break
                print let + ": " + str(singles[let])
                ten += 1

            ten = 0
            # iterate through top ten, show them!
            # SHOWS Doubles!
            print "\nPair Freq:"
            for let in x:
                if ten == 10:
                    break
                print let + ": " + str(doubles[let])
                ten += 1

            ten = 0
            # iterate through top ten, show them!
            # SHOWS Triples!
            print "\nTriplets Freq:"
            for let in y:
                if ten == 10:
                    break
                print let + ": " + str(triples[let])
                ten += 1
    else:
        singOut = ""
        doubOut = ""
        tripOut = ""
        
        # Create strings for pinting
        for let in z:
            singOut += "{" + let + ": " + str(singles[let]) + "},"
        singOut = singOut[:-1] 
        for let in x:
            doubOut += "{" + let + ": " + str(doubles[let]) + "},"
        doubOut = doubOut[:-1]
        for let in y:
            tripOut += "{" + let + ": " + str(triples[let]) + "},"
        tripOut = tripOut[:-1]

        print "Singles: \n" +   singOut
        print "\nDoubles: \n" + doubOut
        print "\nTriples: \n" + tripOut
