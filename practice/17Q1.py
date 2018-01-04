import sys

def reverse(a):
   i = 0
   while i < len(a):
      j = len(a) - i
      tmp = a[i]
      a[j] = tmp
      a[i] = a[j]
      i = i + 1

a = sys.argv[1]
reverse(a)

print " ".join(a)