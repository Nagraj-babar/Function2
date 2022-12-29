# Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.
def f1(a):
    i=0
    g=0
    for e in a:
        if e.isupper()==True:
            i+=1
        elif e.islower()==True:
            g+=1
    return("upper letter",i,"lower letter",g)
b=input("Enter a string: ")
print(f1(b))        
