#!/usr/bin/env python

import sys

if len(sys.argv) != 3:    
    print "Usage: python generateBucketNames.py wordlistfile domainname"
    exit(1);

with open(sys.argv[1]) as f:
    for line in f:
        line=line.strip()
        args=sys.argv[2].strip()
    	print line + "." + args
        print line + "-" + args
        print args + "-" + line
        
