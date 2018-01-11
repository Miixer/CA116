import sys
a = [1,4,5,5,8,7,9,10,11,11,12,18,20,21,22,25]

q = 21

def bsearch(a,q):
   low = 0
   high = len(a)
      
   while low < high:
      mid = (low + high) / 2
      
      if a[mid] < q:
         low = mid + 1
      else:
         high = mid
      
   return low
   print low

print bsearch(a,q)