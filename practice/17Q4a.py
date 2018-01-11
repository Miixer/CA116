a = [67, 4, 45, 22, 89, 3, 97, 12]

i = 0
smallest = 0
while i < len(a):
   j = smallest = i
   while j < len(a):
      if a[j] < a[smallest]:
         smallest = j
      j = j + 1
   a[i], a[smallest] = a[smallest], a[i]
   print a[i]
   i = i + 1

