# Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.
l1=[10,20,30,10,10,40]
def f1(a):
    b=set(a)
    c=sorted(b)
    return c
print(f1(l1))