#5.2
x = 1


var = (2 if x >= 1 else 0)

xyz = (var *2 if(var != 0) else x*2)
print(var)
print(xyz)

#5.2.1 ,5,2,2 ,5.2.3
import random

n = random.randint(1,10)

#Whenever while is finished else would be triggered by either while condition being false 
#Else will not be executed when break is invoked
attempt = 0
while attempt != n:
    attempt = int(input("Enter a number:"))
    if attempt == n + 1 or attempt == n - 1:
        print("You're off by one")
else:
    print("loop break")
    print(f"You did it! You cracked the code which is:{n}")


#This is my factorial function


def factorial(num):
    ans = 1
    for i in range(num):
        
        ans *= num - i
        
    return ans


#This is a while true representation of it

"""
Continue -> Restarts loop
Break stops loop
"""
while True:
    if input("Should we run fibonacchi[Y/N]?:") == "N":
        break
    else:
        num = int(input("Enter a number?:"))
        ans = 1
        ans *= num
        if num < 0:
            print("Number cannot be negative")
            continue

        numdex = num - 1
        while numdex > 0:
            print(numdex)
            ans *= numdex
            numdex -= 1
        print(ans)
print("Program aborted by user")
