#Factorial of a number

print("Let's find the factorial of a number !")
n = int(input("Number: "))
def factorial(n):
    fac = 1
    for i in range(1,n+1): #because it is closed at upper limit
        fac = fac * i
    return fac

print(factorial(n))

print("Now let's see if we can use it in permutations to find out how many ways red and blue balls can be arranged.\nPlease input the number of the same.")
b = int(input("Number of blue balls: ")); bf = factorial(b)
r = int(input("Number of red balls: ")); rf = factorial(r)

total = factorial(b+r)
perms = total/(bf*rf)

print("The number of ways you can arrange",b,"blue balls and",r,"red balls is",perms)