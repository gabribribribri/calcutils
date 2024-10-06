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

for i in range(2, int(to_dec/2)+2) :
    if is_prime(i) :
        while True:
            if to_dec%i == 0 :
                print("{} | {}".format(int(to_dec), i))
                to_dec /= i
            else :
                break
    if to_dec == 1:
        break

print("1 |")