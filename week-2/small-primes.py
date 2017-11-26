n = input()
if n >= 2:
   for i in range(2,n):
      if (n % i) == 0:
         print "not prime"
         break 
   else:
      print "prime"
else:
   print "not prime"