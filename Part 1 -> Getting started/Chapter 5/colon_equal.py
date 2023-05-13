if y:= 6*6:
    print(36)
print(y)
tri = 1
secret = 3000

while((attempt:=int(input("Enter num?:"))) != secret):
   
    if attempt > secret:
        print("Too large by:", attempt - secret)
    else:
        print("Too small by:", secret-attempt)
    tri += 1
else:
    print("Just right it is",secret)
    print(tri, " try to crack the puzzle")