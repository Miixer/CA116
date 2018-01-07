def play():
   i = 0
   while i < n and secret_number.guess(i) != "correct":
      i = i + 1