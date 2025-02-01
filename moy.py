from inlib import parse_input

tm = 0.0
te = 0

while True:
  im = parse_input("in ", {str.isdecimal:"decimal 'in' only"})
  if im is None:
    break
  co = parse_input("co ", {str.isdigit:"digits 'co' only"})
  if co is None:
    break
  tm+=float(im)*float(co)
  te+=float(co)

print("->",tm/te)  
