a=int(input("How far would you like to travel in miles?"))

if a<3:
  print("I suggest Bicycle to your destination")
elif a>3 and a<300:
  print("I suggest Motor-Cycle to your destination")
else:
  print("I suggest Super-Car to your destination")
