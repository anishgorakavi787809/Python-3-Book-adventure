#5.2
x = 1


var = (2 if x >= 1 else 0)

xyz = (var *2 if(var != 0) else x*2)
print(var)
print(xyz)

#5.2.1 ,5,2,2 ,5.2.3
import random

n = random.randint(1,10)

#Whenever while is finished else would be triggered by either while condition being false or by "break" statement
attempt = 0
while attempt != n:
    attempt = int(input("Enter a number:"))
    if attempt == n + 1 or attempt == n - 1:
        print("You're off by one")
else:
    print("loop break")
    print(f"You did it! You cracked the code which is:{n}")