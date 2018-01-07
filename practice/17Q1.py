import sys

def reverse(a):
   i = 0
   while i < len(a) / 2:
      j = len(a) - 1 - i
      tmp = a[i]
      a[i] = a[j]
      a[j] = tmp
      i = i + 1
   return(a)

a = sys.argv[1].strip().split()
print a
reverse(a)

print " ".join(a)
