import sys

def add(num1,num2):
  addition = num1 + num2
  return addition

def sub(num1,num2):
  sub = num1 - num2
  return sub

def mul(num1,num2):
  mul= num1 * num2
  return mul

num1=float(sys.argv[1])
operation = sys.argv[2]
num2=float(sys.argv[3])

if operation == "add":
  output = add(num1, num2) 
  print(output)
