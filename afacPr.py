def is_prime(x) :
    for i in range(2, int(x**0.5)+1):
        if x%i == 0 :
            return False
    return True

while True :
    try:
        to_dec = int(input("> "))
    except :
        print("non.")
        continue
    break

if is_prime(to_dec):
    print("Prime !!")
    exit()

fac_pr = {}
for i in range(2, to_dec+1) :
    if is_prime(i) :
        expo_i = 0
        while True:
            if to_dec%i == 0 :
                print("{} | {}".format(int(to_dec), i))
                to_dec /= i
                expo_i = 0
            else :
                if expo_i != 0:
                    fac_pr[i] = expo_i
                break
    if to_dec == 1:
        break

print("1 |\n")

for (coef, expo) in fac_pr.items():
    print("{}^{}*".format(coef, expo))

