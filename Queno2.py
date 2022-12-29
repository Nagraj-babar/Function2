# Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.
def f1(a):
    for i in range(2,a+1):
        if a%i==0:
            return "Not a prime Number"
        else:
            return "Prime Number"    
b=int(input('Enter a number: '))
print(f1(b))