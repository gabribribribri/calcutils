# OUTDATED
# use facPr insted

print("(criteres divs)")

while True :
    try :
        to_dec = int(input("> "))
    except :
        print("non.")
        continue
    break

nbre_premiers = []
is_prime      = True

print("sqrt={}".format(to_dec**0.5))
for i in range(2, int(to_dec**0.5)+1) :
    is_prime = True
    for j in range(2, int(i**0.5)+1) :
        if i%j == 0 :
            is_prime = False
            break
    
    if is_prime :
        nbre_premiers += [i]


is_prime = True

for i in nbre_premiers :
    print("/ {} = {}".format(i, to_dec/i))

    if to_dec%i == 0 :
        is_prime = False
        num_not  = i
        break

if is_prime :
    print("Prime !")
else :
    print("Pas prime :", i)
