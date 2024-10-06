import random

p,f,y=0,0,1

while True :
  print("tour",y)
  x=random.randint(0,1)
  
  if x == 0:
    print("\n\n       <PILE>")
    p+=1
  else:
    print("\n\n       <FACE>")
    f+=1
  print("{}p  {}f\n%f={}".format(p,f,f/(p+f)*100))
  input(">> ")
  y+=1