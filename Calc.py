def Calc():
  print("Calc by EntityAiden")
  print("-------------------")
  print("| 1. Addition     |")
  print("| 2. Subtraction  |")
  print("| 3. Mutiplcation |")
  print("| 4. Divition     |")
  print("-------------------")
  print()
  
IDK = input()

if IDK == 1:
  NUM1 = input("First number? ")
  NUM2 = input("Second number? ")
  print(NUM1 + NUM2)
  print("prog ended")

if IDK == 2:
  NUM1 = input("First number? ")
  NUM2 = input("Second number? ")
  print(NUM1 - NUM2)
  print("prog ended")

if IDK == 3:
  NUM1 = input("First number? ")
  NUM2 = input("Second number? ")
  print(NUM1 * NUM2)
  print("prog ended")

if IDK == 4:
  NUM1 = input("First number? ")
  NUM2 = input("Second number? ")
  print(NUM1 / NUM2)
  print("prog ended")
