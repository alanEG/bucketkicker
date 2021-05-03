#!/usr/bin/python3 

import sys

if len(sys.argv) != 3:
    print("Usage: python generateBucketNames.py wordlistfile domainname")
    exit(1);

with open(sys.argv[1]) as f:
    lines=line.strip()
    args=sys.argv[2].strip()
    for line in f:
        print(lines + "." + args)
    for line in f:
        print(args + "." + lines)
    for line in f:
        print(lines + "-" + args)
    for line in f:
        print(args + "-" + lines)
    for line in f:
        print(args + lines)
    for line in f:
        print(lines + args)
