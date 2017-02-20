""" 
Project: algorithms-exercises-using-python
Created by robin1885@github on 17-2-20.
"""
import timeit


popzero = timeit.Timer("x.pop(0)",
                       "from __main__ import x")
popend = timeit.Timer("y.pop()",
                      "from __main__ import y")

if __name__ == "__main__":
    x = list(range(2000000))
    print popzero.timeit(number=1000)

    y = list(range(2000000))
    print popend.timeit(number=1000)
