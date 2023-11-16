# 1. Please complete the following:
#   Your First name and Last Name: Celia Shi
#   Your Student ID: 261175554

# 2. Write your program here: 

#GLOBAL VARIABLES:
RIGHT_DIR = 1
LEFT_DIR = -1

def is_outside_list(letter_list, index):
    """(list[str], int) -> bool
    Checks if the given list has the given index

    >>> el = ["A","B","C","D","E"]
    >>> is_outside_list(el, 4)
    False
    >>> el = ["A","B","C","D","E"]
    >>> is_outside_list(el, 9)
    True
    >>> el = ["A","B","C","D","E"]
    >>> is_outside_list(el, -3)
    True
    """

    length = len(letter_list) - 1
    if index > length or index < 0:
        return True
    else:
        return False
    
def letter_positions(letter_list, char):
    """(list[str], str) -> list[int]
    Returns a list of indices where the char is found. If it finds none, retruns an empty list

    >>> el = ["A","B","C","D","E", "A"]
    >>> letter_positions(el, "A")
    [0, 5]
    >>> el = ["A","B","C","D","E", "A"]
    >>> letter_positions(el, "E")
    [4]
    >>> el = ["A","B","C","D","E", "A"]
    >>> letter_positions(el, "G")
    []
    """
    list = []
    index = 0
    for el in letter_list:
        if el == char:
            list.append(index)
        index += 1
    return list

def valid_word_pos_direction(letter_list, word, index, direction):
    """(list[str], str, int, int) -> bool
    Checks if the word is found in the list, reading from right to left or
    left to right depending on the direction

    >>> el = ["A","B","C","D","E","F"]
    >>> valid_word_pos_direction(el, "BCD", 1, 1)
    True
    >>> el = ["A","B","C","D","E","F"]
    >>> valid_word_pos_direction(el, "EDC", 4, -1)
    True
    >>> el = ["A","B","C","D","E","F"]
    >>> valid_word_pos_direction(el, "FEW", 4, 1)
    False
    >>> el = ["A","B","C","D","E","F"]
    >>> valid_word_pos_direction(el, "BCD", 9, 1)
    False
    """  

    word_length = len(word)
    count = 0

    for i in range(word_length):
        if not is_outside_list(letter_list, index):
            if letter_list[index] == word[i]:
                count += 1
                index += direction
                i += 1
    if count == word_length:
        return True
    else:
        return False

def direction_word_given_position(letter_list, word, index):
    """(list[str], str, int) -> list[int]
    Returns a list of direction in which you can find the word in
    
    >>> el = ["A","B","C","D","E","D"]
    >>> direction_word_given_position(el, "BCD", 1)
    [1]
    >>> el = ["A","B","C","D","E","D"]
    >>> direction_word_given_position(el, "ED", 4)
    [-1, 1]
    >>> el = ["A","B","C","D","E","D"]
    >>> direction_word_given_position(el, "CM", 9)
    []
    """

    list = []
    if not is_outside_list(letter_list, index):
        if letter_list[index] == word[0]:
            if valid_word_pos_direction(letter_list, word, index, LEFT_DIR):
                list.append(LEFT_DIR)
            if valid_word_pos_direction(letter_list, word, index, RIGHT_DIR):
                list.append(RIGHT_DIR)
    return list

def position_direction_word(letter_list, word):
    """(list[str], str) -> list[list[int]]
    returns a nested list of the position and direction of the word

    >>> el = ["A","B","C","D","E","D"]
    >>> position_direction_word(el, "ABC")
    [[0, 1]]
    >>> el = ["A","B","C","D","E","D"]
    >>> position_direction_word(el, "DE")
    [[3, 1], [5, -1]]
    >>> el = ["F","C","F","C","Q"]
    >>> position_direction_word(el, "FC")
    [[0, 1], [2, -1], [2, 1]]
    """

    main_list = []
    list_index = letter_positions(letter_list, word[0])
    for el in list_index:
        list_dir = direction_word_given_position(letter_list, word, el)
        for n in list_dir:
            list = [el, n]
            main_list.append(list)
    return main_list

def cross_word_position_direction(bool_letter_list, length_word, index, direction):
    """(list[bool], int, int, int) -> none 
    Replaces the values of the list depending on the length of the word, 
    where it starts and the direction
    
    >>> el = [False, False, False, False, False, False]
    >>> cross_word_position_direction(el, 2, 0, 1)
    [True, True, False, False, False, False]
    >>> el = [False, False, False, False, False, False]
    >>> cross_word_position_direction(el, 5, 1, -1)
    [True, True, False, True, True, True]
    >>> el = [False, False, False, False, False, False]
    >>> cross_word_position_direction(el, 1, 5, -1)
    [False, False, False, False, False, True]
    """

    for i in range(length_word):
        if not is_outside_list(bool_letter_list, index):
            bool_letter_list[index] = True
        index += direction
el = [False, False, False, False, False, False]
cross_word_position_direction(el, 5, 1, -1)
print(el)
def cross_word_all_position_direction(bool_letter_list, len_word, list_pos_dir):
    """(list[bool], int, list[list[int]]) -> none
    replaces the value of the list according to all the position and direction of a given word

    >>> el = [False, False, False, False, False, False, False, False]
    >>> cross_word_all_position_direction(el, 3, [[0,1],[6,-1]])
    [True, True, True, False, True, True, True, False]
    >>> el = [False, False, False, False, False, False]
    >>> cross_word_all_position_direction(el, 2,  [[3, -1], [3, 1]])
    [False, False, True, True, True, False]
    >>> el = [False, False, False, False, False, False]
    >>> cross_word_all_position_direction(el, 1, [[0, -1]])
    [True, False, False, False, False, False]
    """

    for el in list_pos_dir:
        cross_word_position_direction(bool_letter_list, len_word, el[0], el[1])

def find_magic_word(letter_list, bool_letter_list):
    """(list[str], list[bool]) -> str
    compares the list of booleans and the list of characters to find the magic word
    
    >>> el = ["H", "G", "I", "L", "E", "R", "T", "O"]
    >>> bool = [False, True, False, True, True, True, True, True]
    >>> find_magic_word(el, bool)
    HI
    >>> el = ["C", "A", "B", "D", "O", "M", "P"]
    >>> bool = [False, True, True, True, False, False]
    >>> find_magic_word(el, bool)
    ValueError: Both lists should have the same size
    >>> el = ["C", "A", "B", "D", "O", "M", "P"]
    >>> bool = [True, True, True, True, True, True, True]
    >>> find_magic_word(el, bool)
    ""
    """

    i = 0
    magic_word = []
    if len(letter_list) != len(bool_letter_list):
        raise ValueError("Both lists should have the same size")
    
    for el in letter_list:
        if bool_letter_list[i] != True:
            magic_word.append(el)
        i += 1
    
    word = "".join(magic_word)
    return word

def word_search(letter_list, word_list):
    """(list[str], list[str]) -> str
    Finds the word from a list of characters and a list of words
    
    >>> letter_list = ["H", "G", "I", "L", "E", "R", "T", "O"]
    >>> word_list = ['G','LERTO']
    >>> word_search(letter_list, word_list)
    HI
    >>> letter_list = ['E', 'Y', 'E', 'H', 'E', 'Y', 'O', 'L', 'L', 'O']
    >>> word_list = ['EYE','YO']
    >>> word_search(letter_list, word_list)
    HELLO
    >>> letter_list = ['P', 'W', 'N', 'F', 'O', 'J', 'R','L', 'D']
    >>> word_list = ['P','NF',"J"]
    >>> word_search(letter_list, word_list)
    WORLD
    """
    for el in word_list:
        positions = position_direction_word(letter_list, el)
        cross_word_all_position_direction(letter_list, len(el), positions)
    word = find_magic_word(letter_list, letter_list)
    return word

def word_search_main(letters, words):
    """(str, str) -> str
    converts the string of characters into a list and seperates the word, compares them to remove
    all the words in the string and returns the remaining letters

    >>> letters = "PjAVA++CJSYLQSPHPTGOHNILTOKOmatLABNTFIWSRUSTYBURTRAd"
    >>> words = "java-C++-JS-SQL-php-GO-kotlin-MATLaB-SWIFT-RUSt-ruby-DART"
    >>> word_search_main(letters, words)
    PYTHON
    >>> letters = "HhoopELlineLfrogO"
    >>> words = "Hoop-LiNE-FRog"
    >>> word_search_main(letters, words)
    HELLO
    >>> letters = "rollWtreeORENilLD"
    >>> words = "ROlL-trEE-LIne"
    >>> word_search_main(letters, words)
    WORLD
    """
    
    list_char = list(letters.upper())
    list_word = words.upper().split("-")
    secret_word = word_search(list_char, list_word)
    return secret_word