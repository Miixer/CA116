import sys

d = {}

with open("german.txt", "r") as f:
   lines = f.readlines()
   i = 0
   while i < len(lines):
      line = lines[i].strip().split()
      d[line[0]] = line[1]
      i = i + 1

   print d


with open("english.txt", "r") as s:
   words = s.read().split()
   for word in words:
      print d[word]