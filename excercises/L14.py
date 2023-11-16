#exercise 1
data = {"Fall 2017": 816, "Winter 2018": 613, "Fall 2018": 709, "Winter 2019": 590, "Fall 2019": 744 }
count = 0
total = 0

for el in data:
    total += data[el]
    count += 1

average = total/count
print(average) #could'Ve used len(data) instead of count variable

#exercise 2
def counting(input):
    count = {}
    for el in input:
        if el[0].isupper(): # should always check if length is not 0, so there arent any debugging errors
            if el[0] in count:
                count[el[0]] += 1
            else:
                count[el[0]] = 1
    
    print(count)

# list = ["Aljfd", "doife", "ofkSkj", "Lobnfjkdn", "Lijfiodi"]
# counting(list)

#exercise 3
def alph_check(to_check, alph):
    data = dict.fromkeys(alph, False)
    for el in to_check:
        if el in data:
            data[el] = True
    print(data)

# alph_check("banana", "bac")
