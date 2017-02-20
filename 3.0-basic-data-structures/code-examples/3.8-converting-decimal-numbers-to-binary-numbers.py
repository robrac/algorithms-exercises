""" 
Project: algorithms-exercises-using-python
Created by robin1885@github on 17-2-20.
"""


from pythonds.basic.stack import Stack


def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber //= 2

    binString = ""
    while not remstack.isEmpty():
        binString += str(remstack.pop())

    return binString


def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]

    return newString


print(divideBy2(42))
print(baseConverter(25, 2))
print(baseConverter(25,16))