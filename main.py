"""
practice python

NOTE:
Run any python command as:
e.g. 
py -m pip install pytest
py -m pip --version

"""

import sys

def firstFunction():
    msg = "\nHello, This is my first python program in VS code!"
    print(msg)

x = 1
if x==1:
    print("x if ", x)

def increment(x):
    return x + 1

def decrement(x):
    return x - 1

def main():
    x=10
    # increment(x)
    print("main: value of x= ", x)
    firstFunction()
    

    print("Good Bye!")

if __name__ == "__main__":
    main()