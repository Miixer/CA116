#!/usr/bin/env python

import sys
import math

def plus(a,b):
   return a + b

def minus(a,b):
   return a - b

def multiply(a,b):
   return a * b

def divide(a,b):
   return a / b

def remainder(a,b):
   return a % b

def power(a,b):
   return a ** b

def neg(a):
   return -a

def square(a):
   return a * a

def sqr(a):
   return math.sqrt(a)

def log(a):
   return math.log(a)

binary_operators = {
   "+": plus,
   "-": minus,
   "*": multiply,
   "/": divide,
   "%": remainder,
   "**": power,
}

unary_operators = {
   "n": neg,
   "s": square,
   "r": sqr,
   "l": log,
}

def is_int(s):
   return s.isdigit() or (2 <= len(s) and s[0] == "-" and s[1:].isdigit())

def is_float(s):
   a = s.split(".")
   return len(a) == 2 and int(a[0]) and a[1].isdigit()
   #return (2 <= len(s) and s[1] == "." and s[2:].isdigit() or s[0] == "-" and s[4:].isdigit())

def rpn(stack, op):
   if is_int(op):
      stack.append(int(op)) 
   elif is_float(op):
      stack.append(float(op)) 
   elif op in binary_operators:
      b = stack.pop()
      a = stack.pop()
      c = binary_operators[op](a,b)
      stack.append(c)
   elif op in unary_operators:
      a = stack.pop()
      b = unary_operators[op](a)
      stack.append(b)
   elif op == "p":
      print stack[len(stack)-1]

stack = []

line = sys.stdin.readline()
while 0 < len(line):
   ops = line.split()
   i = 0
   while i < len(ops):
      rpn(stack, ops[i])
      i = i + 1
   line = sys.stdin.readline()