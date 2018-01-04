import sys
inp = sys.argv[1]

with open(inp) as f:
   text = f.readlines()
   
   i = 0
   while i < len(text):
      line = text[i].split()
      #print line[1:]
      date = line[0].split("/")
      names = line[1:]
      if date[2] > "70":
         print " ".join(names)
      i += 1
      #print date
      