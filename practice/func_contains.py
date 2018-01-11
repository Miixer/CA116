import sys
import func_bsearch

a = [2,3,6,6,7,8]
q = 2

def contains(a,q):
   p = func_bsearch.bsearch(a,q)
   return p < len(a) and a[p] == q

contains(a,q)