a = [1,2,3,4,5]

i = 0
while i < len(a) / 2:
   tmp = a[i]
   a[i] = a[len(a) - i - 1]
   a[len(a) - i - 1] = tmp 
   i = i + 1

print a