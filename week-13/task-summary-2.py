import sys

d = {}

with open("task-sum.txt", "r") as f:
   lines = f.readlines()

   for line in lines:
      line = line.strip().split("/")
      status = line[1].split(".")
      
      #if line[0] not in d:
      d[line[0]] = status[2]

      print line
   for line in d:
      if d[line] == "correct":
         d[line] = 1
      else:
         d[line] = 0

print d


