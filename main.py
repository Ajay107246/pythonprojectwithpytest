"""
practice python

NOTE:
Run any python command as:
e.g. 
py -m pip install pytest
py -m pip --version

"""

import sys
import requests

def len_url():
    ret_url = get_url()
    print(ret_url)
    return len(ret_url)

def get_url():
    check_url = "https://www.google.de"
    
    """response = requests.get(check_url)

    # print(response)
    if response.status_code == 200:
        joke = response.json()['value']['joke']
        # joke = response.content
    else:
        joke = 'No joke'
    """
    return check_url
    

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
    result = get_url()
    print(result)
    len_url_google = len_url()
    print(len_url_google)

    print("Good Bye!")

if __name__ == "__main__":
    main()