def function1(x,y):
    avg=(x+y)/2
    return avg

a=int(input("Enter first number -\n"))
b=int(input("Enter second number -\n"))

ans=float(function1(a,b))
print("Average =",ans)