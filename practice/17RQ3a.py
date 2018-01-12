a = [1,2,3,4,5]

i = 0
while i < len(a) / 2:
   tmp = a[i]
   print tmp
   a[i] = a[len(a) - i - 1]
   print a[i]
   a[len(a) - i - 1] = tmp
   print tmp     
   i = i + 1

print a