def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n-2)
for n in range(1, 4):
    print(f"{n} : {fib(n)}" )

for number in range(1,11):
    print(f"{number}: {fib(number)}")

f_cache = {}
value = 0

def fib2(number):

    if number in f_cache:
        return f_cache[number]
    if number == 1:
        value =1
    elif number == 2:
        value = 1
    elif number > 2:
        value = fib2(number-1) + fib2(number-2)

    f_cache[number] = value
    return value

#for n in range (1,500):
 #  print(f"{n}: {fib2(n)}")

from functools import lru_cache
#Least Recently Used Cache

#memoization
@lru_cache(maxsize=100)
def fib3(k):
    if k == 1 or k == 2:
        return 1
    elif k > 2:
        return fib3(k-1) + fib3(k-2)

#for i in range(999):
 #   print(f"{i}: {fib3(i)}")

def TowerOfHanoi(n, source, destination_rod, auxiliary_rod):
    t=0
    if n == 1:
        print("Move disk 1 from source ", source, " to destination ", destination_rod)

        print(t)
        t+=1
        return
    TowerOfHanoi(n - 1, source, auxiliary_rod, destination_rod)
    print("Move disk ", n, " from source ", source, " to destination ", destination_rod)
    TowerOfHanoi(n - 1, auxiliary_rod, destination_rod, source)

n = 
TowerOfHanoi(n, 'A', 'B', 'C')