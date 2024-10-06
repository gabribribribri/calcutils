tm = 0.0
te = 0

while True:
  try:
    im=input("in ")
    if im=="b":
      break
      
    im = float(im)
    co = int  (input("co "))
  except:
    print("non")
    continue
    
  tm+=im*float(co)
  te+=co

print("->",tm/te)  