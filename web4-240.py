def FindAllInverse():
    mod = int(input("Whats the mod: "))
    for n in range(0, mod):
        inverse = n
        el = mod
        while el != 0:
            remainder = n % el
            n = el
            el = remainder  
        if n == 1:
            print(inverse)

def FermatSTheory():
    mod = int(input("whats the mod: "))
    max = int(input("whats the range: "))
    exp = int(input("whats the exponent: "))
    num = int(input("whats the wanted number in that mod: "))
    for n in range(0, max):
        remainder = (n**exp)% mod 
        if remainder == num:
            print(n)

# FermatSTheory()

def FermatModified():
    mod = int(input("whats the mod: "))
    max = int(input("whats the range: "))
    exp = int(input("whats the exponent: "))
    for n in range(0, max):
        remainder = (n**exp)% mod 
        if remainder == n:
            print(n)

# FermatModified()

def getRemainder():
    mod = int(input("whats the mod: "))
    num = int(input("whats the base: "))
    exp = int(input("whats the exponent: "))
    remainder = (num**exp)% mod 
    print(remainder)

# getRemainder()

def prob8a():
    mod = int(input("whats the mod: "))
    mult = int(input("whats the multiplier: "))
    num = int(input("whats the wanted number in that mod: "))
    for n in range(0, mod):
        remainder = (mult*n) % mod
        if remainder == num:
            print(n)

# prob8a()

def prob8b():
    mod = int(input("whats the mod: "))
    num = int(input("whats the wanted number in that mod: "))
    for n in range(0, mod):
        remainder = (n**2 - 3*n + 2) % mod
        if remainder == num:
            print(n)

# prob8b()

def RSAdecoder():
    s = int(input("what is s: "))
    n = int(input("what is n: "))
    while True:
        m = int(input("what is M: "))
        num = (m **29) % 91
        print(num)

# RSAdecoder()