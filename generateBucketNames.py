#!/usr/bin/python3 

import sys

if len(sys.argv) != 3:
    print("Usage: python generateBucketNames.py wordlistfile domainname")
    exit(1);

with open(sys.argv[1]) as f:
    for line in f:
        lines=line.strip()
        args=sys.argv[2].strip()
        print(line.strip() + "." + args.strip())
        print(lines.strip() + "-" + args.strip())
        print(args.strip() + "-" + lines.strip())
        print(arfs.strip() + lines.strip())
