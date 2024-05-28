def Calc():
  from core import Core
  import os
  os.system("clear")
  print("Calc by EntityAiden")
  print("-------------------")
  print("| 1. Addition     |")
  print("| 2. Subtraction  |")
  print("| 3. Mutiplcation |")
  print("| 4. Divition     |")
  print("-------------------")
  print()
  
  IDK = input()

  if IDK == "1":
    NUM1 = int(input("First number? "))
    NUM2 = int(input("Second number? "))
    print(NUM1 + NUM2)
    print("prog ended")
    Core()


  if IDK == "2":
    NUM1 = int(input("First number? "))
    NUM2 = int(input("Second number? "))
    print(NUM1 - NUM2)
    print("prog ended")
    Core()

  if IDK == "3":
    NUM1 = int(input("First number? "))
    NUM2 = int(input("Second number? "))
    print(NUM1 * NUM2)
    print("prog ended")
    Core()

  if IDK == "4":
    NUM1 = int(input("First number? "))
    NUM2 = int(input("Second number? "))
    print(NUM1 / NUM2)
    print("prog ended")
    Core()
