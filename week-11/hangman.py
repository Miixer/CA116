#!/usr/bin/env python

import random
import os

dictionary = "words.txt"
guesses = 10

with open(dictionary) as f:
   words = f.read().split()

n = random.randint(0,len(words)-1)
word = words[n]

letters = []

def get_state():
   output = []
   i = 0
   while i < len(word):
      if word[i] in letters:
         output.append(word[i])
      else:
         output.append("_")
      i = i + 1
   return "".join(output)

def next_state(state):
   os.system("clear")
   print
   print state
   print 
   print ", ".join(letters)
   print
   print "Guess a letter:",
   ch = raw_input().strip()
   if len(ch) == 1 and ch not in letters:
      letters.append(ch)
   return get_state()


state = get_state()

i = 0
while i < guesses and state != word:
   old_state = state
   state = next_state(state)
   if state == old_state:
      i = i + 1

if state == word:
   print
   print "correct:", word
   print
else:
   print
   print "incorrect:", word
   print 