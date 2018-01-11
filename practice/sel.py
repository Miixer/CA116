import sys
s = sys.argv[1]
a = []



i = 0
while i < len(a):
   a.append(int(s))
   p = i
   j = i + 1
   while j < len(a):
      if a[j] < a[p]:
         p = j
      j = j + 1

   tmp = a[p]
   a[p] = a[i]
   a[i] = tmp

   i = i + 1

print a