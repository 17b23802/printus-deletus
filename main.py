x = input("Add, Minus, Times or Divide?")
if x == "Add":
  Numbers = input("How many numbers")
  Num1 = int(input("Number one"))
  while Numbers > 1:
    Numbers = Numbers - 1
    NumExtra = int(input("Next Number"))
    Num1 = Num1 + NumExtra
  print(Num1,"is the total!")

elif x == "Minus":
  y = int(input("Number one"))