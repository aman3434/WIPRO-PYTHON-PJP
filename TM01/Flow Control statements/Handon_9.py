a=int(input("Enter a number"))

sum=0

while(a>0):
  ld=a%10
  sum=(sum*10)+ld
  a=a//10

print(sum)
 