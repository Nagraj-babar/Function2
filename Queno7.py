# Write a python program to access a function inside a function.
def f1(a):
    if a==1:
        return 1
    s=a+f1(a-1)
    return s
print(f1(4))