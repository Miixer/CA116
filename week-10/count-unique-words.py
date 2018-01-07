import sys
lines = sys.stdin.read().split()
seen = {}

i = 0
while i < len(lines):
   if lines[i] not in seen:
      seen[lines[i]] = 1
   elif lines[i] in seen:
      seen[lines[i]] = 2
   i = i + 1

i = 0
while i < len(lines):
   if seen[lines[i]] == 1:
      print lines[i]
   i = i + 1