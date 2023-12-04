#exercise 1
def print_with_pipes(input):
    placeholder = []
    for i in input:
        placeholder.append(str(i))
    x = "|".join(placeholder)
    print(x)

# print_with_pipes([1, 2, 3, 4, 5])

#exercise 2
def from_same_letters(word, letters):
    for i in word:
        for j in i:
            if j in letters:
                continue
            else:
                return False
    return True

# w = ["cat", "at", "car"]
# print(from_same_letters(w, "catr"))

#exercise 3
def shift_up(input):
    input[:] = input[-1:] + input[:-1]

# a = [1, 2, 3, 4, 5]
# shift_up(a)
# print(a)

#exercise 4
def print_2D_list(D):
    for i in D:
        for j in i:
            print(j, end=" ")
        print()

# print_2D_list([['owl', 'bat','cow'],['goat','duck', 'lion','bear'],['panda','zebra']])

#exercise 5
#wrong
def min_elements(input):
    smalls = []
    for i in input:
        smallest = 0
        for j in range(len(i)):
            if j < len(i) - 1:
                if i[j] < i[j+1]:
                    smallest = i[j]
                else:
                    smallest = [j+1]
        smalls.append(smallest)
    return smalls

m=[[2, 3, 9], [5,1,6], [8,-1,9]]
print(min_elements(m))
