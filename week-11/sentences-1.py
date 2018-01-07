#!/usr/bin/env python

import sys
line = sys.stdin.readline()

a = []

i = 0
while i < len(line):
   if line[i] == ".":
      j = i
      print line[:i+1]
      line = sys.stdin.readline()
   elif line[i] == "!":
      print line[:j]




   i = i + 1
