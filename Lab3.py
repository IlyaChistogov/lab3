from pyDatalog import pyDatalog
import random
import functools
pyDatalog.create_terms('X, Z, Y, Sum, div, Average, y, SumRand')

(y[X] == sum_(Y, for_each=Y)) <= ((Y._in(range_(X+1))))
print(y[10] == Sum)

(div[X, Y] == Z) <= (X // Y == Z)
print(div[y[10], 10] == Average)

H = sorted([random.choice(range(99999)) for i in range(100)])
print("Median: ", (H[49] + H[50]) / 2)

print (functools.reduce(lambda a, b : a * b, [random.choice(range(99999)) for i in range(100)]))