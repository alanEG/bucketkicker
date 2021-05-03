#!/usr/bin/python3 

import sys

if len(sys.argv) != 3:
    print("Usage: python generateBucketNames.py wordlistfile domainname")
    exit(1);

with open(sys.argv[1]) as f:
    for line in f:
        lines=line.strip()
        args=sys.argv[2].strip()
        print(lines + "." + args)
        print(args + "." + lines)
        print(lines + "-" + args)
        print(args + "-" + lines)
        print(args + lines)
        print()
