#!/usr/bin/python2.7
# Georges Brantley
# PS02, HW 8
import sys


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print 'No text added!'
        print 'Run \'echo file.txt | frequency analysis.py\''
        sys.exit(0)
    print str(sys.argv[1])
