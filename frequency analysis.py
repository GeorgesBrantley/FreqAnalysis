#!/usr/bin/python2.7
# Georges Brantley
# PS02, HW 8
import sys


if __name__ == "__main__":
    # Create a DICT of singles used! Letter is the key, # is the value
    singles = {}

    # SEE IF THERE ARE ARGS
    if len(sys.argv) <= 1:
        print 'No file selected!'
        print 'Run \'./frequency analysis.py   filename\''
        sys.exit(0)
    
    # open file, read it
    with open(sys.argv[1],'r') as f:
        for line in f:
            for x in line:
                # EVERY LETTER IN FILE
                   
                # SINGLES
                if x.isupper():
                    # EVERY CAP LETTER IN FILE
                    if x in singles:
                        # IF its in the dictionary already, increase count
                        singles[x] += 1
                    else:
                        # add to dictionary
                        singles[x] = 1

    # Put dictionary into a sorted array based on value (reverse)
    x = sorted(singles, key=lambda key: singles[key])
    ten = 0
    # iterate through top ten, show them!
    for let in reversed(x):
        if ten == 10:
            break
        print let + ": " + str(singles[let])
        ten += 1
