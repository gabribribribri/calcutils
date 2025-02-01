from inlib import parse_input
a=int(parse_input("> ", {str.isdecimal:"only decimal."}))

for i in range(2,int(a**0.5)+1):
  if a%i == 0:
    print("= {} * {}".format(i, int(a/i)))
    
print("{} + opposes".format(a))
