a = [27,2,6,25]
maximum = 0


i = 0
while i < len(a):
   if maximum < a[i]:
      maximum = a[i]
   i = i + 1
print maximum

