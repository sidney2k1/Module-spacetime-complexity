def num(n,m):
    total=n*m
    print("Number of iterations is 1")
def num2(n,m):
    total=0
    for i in range(1,n+1):
        total+=m
    print("\nNumber of iterations",n)
n=int(input("Enter a for a*b"))
m=int(input("Enter b for a*b"))
num(n,m)
num2(n,m)