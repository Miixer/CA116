import sys

a = sys.stdin.readlines()
graph = {
   "Dublin-Enfield": 78,
   "Enfield-Dublin": 78,
   "Athlone-Cork": 72,
   "Cork-Athlone": 72,
   "Dublin-Cork": 106,
   "Cork-Dublin": 106,
   "Athlone-Bray": 56,
   "Bray-Athlone": 56,
   "Cork-Bray": 62,
   "Bray-Cork": 62,
   "Enfield-Cork": 40,
   "Cork-Enfield": 40,
}

i = 0
while i < len(a):
   tokens = a[i].split()
   src = tokens[0]
   dst = tokens[1]
   distance = int(tokens[2])
   key1 = src + "-" + dst
   key2 = dst + "-" + src
   graph[key1] = distance
   graph[key1] = distance
   i = i + 1

args = sys.argv[1:]
distance = 0

i = 1
while i < len(args):
   key = args[i - 1] + "-" + args[i]
   distance += graph[key]
   i = i + 1
print distance