def gcd_sq(x, y):
    '''(int, int) -> int
    Returns the squared greatest common divisor of x and y.
    >>> gcd_sq(12, 16)
    16
    '''
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x ** 2

def one(x):
    x = three(x) + two(two(three(x)))
    return x
def two(y):
    if y % 2 == 0:
        return y
    return y // 2
def three(z):
    return z - 3
#print(one(5))

x = 5
z = 7
y=6
if x < z:
    print("A", end = " ")
    z = 4
if x < z:
    z = 6
    print("B", end = " ")
else:
    print("hello")
    print("world")