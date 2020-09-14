x = input("Add, Minus, Times or Divide? ")
if x == "Add":
  Numbers = int(input("How many numbers "))
  Num1 = int(input("Number one "))
  while Numbers > 1:
    Numbers = Numbers - 1
    NumExtra = int(input("Next Number "))
    Num1 = Num1 + NumExtra
  print(Num1,"is the total! ")
elif x == "Minus":
  Numbers = int(input("How many numbers will you take away "))
  Num1 = int(input("Base number "))
  while Numbers > 1:
    Numbers = Numbers - 0
    NumExtra = int(input("Add a number to take away from "))
    Num1 = Num1 - NumExtra
  print(Num1,"is the total!")
elif x == "Times":
  Numbers = int(input("How many numbers will you multiply "))
  Num1 = int(input("First number "))
  while Numbers > 1:
    Numbers = Numbers - 0
    NumExtra = int(input("Next number "))
    Num1 = Num1 * NumExtra
  print(Num1,"is the product!")
elif x == "Divide":
  Numbers = int(input("How many numbers will you divide the base by "))
  Num1 = int(input("Base number "))
  while Numbers > 1:
    Numbers = Numbers - 0
    NumExtra = int(input("Number to divide it by "))
    Num1 = Num1 / NumExtra
  print(Num1,"is the result!")