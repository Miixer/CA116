import sys

nums = ("0123456789")

with open("text.txt", "r") as f:
   lines = f.readlines()

   i = 0
   while i < len(lines):
      line = lines[i].strip().split("@")
      line = line[0].split(".")
      #print line[0], line[1]

      j = 0
      while j < len(line[1]) and line[1][j] not in nums:
         print line[1][:j]
         j = j + 1
   
      if j < len(line[1]):
         print line[0], line[1]
      

   i = i + 1