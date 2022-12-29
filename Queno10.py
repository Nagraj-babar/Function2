# Write a python program to create a function to check whether a string is an anagram or not.
def f1(a,b):
    
    if sorted(a)==sorted(b):
        return 'String is anagram'
    else:
        return 'String is not anagram'
k='pot'
l='top'
print(f1(k,l))