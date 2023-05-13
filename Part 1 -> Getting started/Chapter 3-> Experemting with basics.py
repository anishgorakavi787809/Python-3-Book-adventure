print(2 +  3 * 6)

print([1,2,3] + ["w","rizz"])

def factorial(num):
    ans = 1
    for i in range(num):
        
        ans *= num - i
        
    return ans

print(factorial(4))