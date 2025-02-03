#№ 1
x = float(input())
y = 28.3495231
print(y*x)


#№ 2
#C = (5 / 9) * (F - 32)
f = int(input())
c = (5 / 9) * (f - 32)
print(c)


#№ 3  (35 heads and 94 legs) 
a,b = 35, 94
for i in range(35):
    h=35-i
    if 2*h + 4*i ==94:
        print(h , i)


#№ 4
def prime (n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+ 1):
        if n % i == 0:
            return False
    return True
def filter_prime(number):
    return[num for num in numbers if prime(num)]

numbers = list(map(int, input().split()))
print(filter_prime(numbers))


#№ 5
from itertools import permutations

a = str(input())
perms = ["".join(p) for p in permutations(a)]
print(perms)


#№ 6
x = ["we", "are", "ready"]
x.reverse()
print(x)


#№ 7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

'''
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

numbers = input().split()
numbers = [int(num) for num in numbers]

print(has_33(numbers))
'''


#№ 8
def spy_game(nums):
    sequence = [0, 0, 7]  
    index = 0  

    for num in nums:
        if num == sequence[index]: 
            index += 1
            if index == len(sequence): 
                return True
    return False  


numbers = input().split()
numbers = [int(num) for num in numbers] 


print(spy_game(numbers))


#№ 9
import math
def sphere(r):
    v = ( 4 / 3 ) * math.pi * r ** 3
    return v

print (sphere(int(input())))


#№ 10
def unique(s):
    x = []
    for i in s:
        if i not in x:
            x.append(i)
    return x 

s = list ( map ( int , input().split()))
print(unique(s))


#№ 11
def madam(x):
    a = ""
    for i in x:
        a += i
    for o in range( len(a) // 2 ):
        if a[o] != a[ len(a) - o - 1 ]:
            return False
    return True

x = input().split()
print ( madam (x) )


#№ 12
def histogram(nums):
    for num in nums:
        print('*' * num)


numbers = list(map(int, input().split()))
histogram(numbers)


#№ 13
from random import randint

def play():
    num = randint(1,20)
    print("hello ! what is your name?")
    name =input()
    print(f"Well , {name} ,  I am thinking of a number between 1 and 20.")
    x=True
    z=0
    while x :
        number = int(input("Take a guess."))
        z +=1
        if number==num :
            print(f"Good job, KBTU! You guessed my number in {z} guesses!")
            x=False
            break
        if number > num :
            print("Your guess is too high.")
        if number < num:
            print("Your guess is too low")

play()


















