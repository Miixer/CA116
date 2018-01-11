import sys
n = input()

def is_prime(n):
   if n > 1:
      for i in range(2,n):
         if (n % i) == 0:
            return False
      else:
         return True
   else:
      return False
   

result = is_prime(n)
print result