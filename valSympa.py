a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

print("x:")

for x in range(50):
  if (a*x+c)%b==0:
    print(x)
    
  
