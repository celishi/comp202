#exercise 1
def func(inp, i, j):
    placeholder = inp[i]
    inp[i] = inp[j]
    inp[j] = placeholder

# x = [1, 2, 3, 4, 5]
# func(x, 0, 3)
# print(x)

#exercise 2
def phone(num):
    tel = list(num)
    tel.insert(0, "(")
    tel.insert(4, ")")
    tel.insert(8, "-")
    converted = "".join(tel)
    return converted

# x = "5146997818"
# print(phone(x))

def example(x):
    y = []
    for e in x:
        new_e = []
        for n in e:
            new_e.append(n)            
        y.append(new_e)
    y[0][0] = 5
    print(y)

a = [[1, 2], [3, 4], [5]]
example(a)
print(a)
