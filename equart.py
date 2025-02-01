# Average difference between two random number
# Between 1 and 100. Why not.
from random import *
t=100000
a=0
for i in range(t):
  a+=abs(randint(1,101)-randint(1,101))
print(a/t)
