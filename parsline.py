
def foo(x, y):
    return x + y

def foo_1(a, b, c = 2):
    return a + b + c

def foo_2(n):
    def foo_3(m):
        return m + n
    return foo_3

ret1 = foo_2(100);

print(ret1(100))

def foo_4(n):
    m = n**2

def foo_5(*args):
    print(*args)

foo_5(1, 2, "hello")
foo_5()
foo_5(1)

foo_6 = lambda x, y: x + y

print("5 + 6 = ",foo_6(5,6))

a = 0

while a < 5 :
    print(a)
    a = a + 1

b = 0
c = 5

if b :
    b = 0
elif c:
    b = 7

array.

for a in



