""" 
Project: algorithms-exercises-using-python
Created by robin1885@github on 17-2-20.
"""

from pythonds.basic.stack import Stack

s = Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())