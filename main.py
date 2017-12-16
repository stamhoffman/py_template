print("Hello, Python")

a = 10
b = "hello"
c = (1, 2)
d = 5.6
m = bool(0)
f = complex(1,2)


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(m))
print(type(f))
print("f = ", f)
print("f,imag = ", f.imag)
print("f.real = ", f.real)
print("f.conjugate", f.conjugate())

import random

v = random.random()
print("v = ", v * 10)

import math

p = math.pi
print("p =", p)
p = math.sqrt(9)
print("p =", p)

d = 5
n = 7

print("d_id = ", id(d))
print("n_id = ",id(n))

d = n

print("d_id = ",id(d))
print("n_id = ",id(n))

print("dec to bin = ", bin(34))

print(5**2)