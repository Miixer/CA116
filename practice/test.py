import sys
a = sys.argv[1]

i = 0
while i < len(a):
   j = len(a) - i
   tmp = a[i]
   #a[i] = a[j]
   #a[i] = a[j]
   i = i + 1

print a
print a[j]
print tmp 
print i
print " ".join(a) 