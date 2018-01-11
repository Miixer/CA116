#Returns largest Fibonacci number less than n.


import sys
n = input()

def fib(n):
   prev = 0
   curr = 1
   while curr < n:
      print curr
      tmp = curr + prev
      prev = curr
      curr = tmp 

fib(n)







#Fibonacci sequence

#def fib(n):
   #prev = 0
   #curr = 1
   #i = 0
   #while i < n:
      #print curr
      #tmp = curr + prev
      #prev = curr
      #curr = tmp
      #i = i + 1


