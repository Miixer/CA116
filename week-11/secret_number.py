num = 60

def guess(inp): 
   if num < inp:
      return "too-high"
   elif num > inp:
      return "too-low"
   elif num == inp:
      return "correct"

def play():
   i = 0
   while i < num and guess(i) != "correct":
      i = i + 1



def main():
   num = 60
   inp = input()
   j = 0
   while j < 10:
      play()
      print guess(inp)
      inp = input()
      j = j + 1

if __name__ == "__main__":
   main()