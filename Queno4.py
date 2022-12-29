# Write a python program to create a function that checks whether a passed string is palindrome or not.
def f1(a):
    b=a[::-1]
    if a==b:
        return "Palindrome"
    else:
        return "Not palindrome"
c=input("Enter a String: ")  
print(f1(c))         