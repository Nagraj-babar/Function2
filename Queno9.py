# Write a python program to create a function to check whether a string is a pangram or not.
def f1(a):
    b="abcdefghijklmnopqrstuvwxyz"
    l='ABCDEFGHIJKMNOPQRSTUVWXYZ'
    for e in a:
     if e.isupper():
        i=str(e) in l
     else:    
        j=str(e) in b
    g=len(a)
    if g>=26:    
        if i or j==True:
            return 'Pangram'
    else:
            return 'Not Pangram'      
s=input("entre a string: ")
print(f1(s))