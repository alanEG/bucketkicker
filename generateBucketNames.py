#!/usr/bin/python3 

import sys

if len(sys.argv) != 3:
    print("Usage: python generateBucketNames.py wordlistfile domainname")
    exit(1);

with open(sys.argv[1]) as f:
    args=sys.argv[2].strip()
    for line in f:
        print(line.strip() + "." + line.strip())
    for line in f:
        print(line.strip() + "." + line.strip())
    for line in f:
        print(line.strip() + "-" + line.strip())
    for line in f:
        print(line.strip() + "-" + line.strip())
    for line in f:
        print(line.strip() + line.strip())
    for line in f:
        print(line.strip() + line.strip())
