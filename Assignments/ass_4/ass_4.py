import pickle

def read_text(text_path):
    try:
        file = open(text_path, "r")
        comments = []
        for line in file:
            line_content = line.split(',')[1]
            comments.append(line_content)
        file.close()
        return comments
    except FileNotFoundError:
        print("File does not exist")

# print(read_text("posts.txt"))
# [" I love this movie! It's great and funny. I am always happy to see it again!\n", ' By the time I got the game to work I was just angry and sad. It is a terrible video game! \n', ' How do I feel about this restaurant? meh! I am indifferent.\n', ' This is 
# a great pizza place!!! I recommend it!\n']

def read_pickle(path_to_pickle):
    file = open(path_to_pickle, "rb")
    content = pickle.load(file)
    file.close()
    return content

# read_pickle("sentiment_dictionary.pkl")

def sentiment_frequencies(text, dictionary_word):
    word_list = text.split(" ")
    sentiment = dictionary_word.keys()
    frequencies = dict.fromkeys(sentiment, 0)

    #counts if the word is in
    for word in word_list:
        for sentiment in dictionary_word:
            if word in dictionary_word[sentiment]:
                frequencies[sentiment] += 1

    for i in frequencies:
        frequencies[i] = round(frequencies[i]/len(word_list), 2)
    
    return frequencies

# dicti = {'POSITIVE': ['great', 'love', 'recommend', 'laugh', 'happy', 'brilliant'], 'NEGATIVE': ['terrible', 'awful', 'hideous', 'sad', 
# 'cry', 'bad'], 'NEUTRAL': ['meh', 'indifferent', 'ignore']}
# phrase = "i love this movie it is great and the adventure scenes are fun i highly recommend it but the theatre was terrible and there was an awful smell"
# sentiment_frequencies(phrase, dicti)

def compute_polarity(dict_frequency):
    largest_num = 0
    for key in dict_frequency:
        if dict_frequency[key] > largest_num:
            largest_num = dict_frequency[key]

    for key in dict_frequency:
        if dict_frequency[key] == largest_num:
            return key

# print(compute_polarity({'POSITIVE': 0.5, 'NEGATIVE': 0.11, 'NEUTRAL': 1}))

def analyse_text(text_path, dict_path):
    content = read_text(text_path)
    sentiment_dict = read_pickle(dict_path)
    stop_words = ["!", ".", ",", "?", ";", "\n"]
    list_polarity = []

    for comment in content:
        converted = comment.lower().strip().split(" ")
        for word in converted:
            for character in stop_words:
                if character in word:
                    converted[converted.index(word)] = word.replace(character, "")
        formatted_comment = " ".join(converted)
        frequencies = sentiment_frequencies(formatted_comment, sentiment_dict)
        polarity = compute_polarity(frequencies)
        list_polarity.append(polarity)

    return list_polarity

# print(analyse_text("posts.txt", "sentiment_dictionary.pkl"))

# PART B

class Company():
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def update_location(self, new_location):
        self.location = new_location

# company = Company("apple", "mtl")
# company.update_location("toronto")

class JobOffer():
    def __init__(self, title, company, contract, salary, description):
        self.title = title
        self.company = company
        self.contract = contract
        self.salary = salary
        self.description = description

    def update_description(self, new_description):
        self.description = new_description

    def __str__(self):
        title = "Title: " + self.title + "\n"
        company = "Company Name: " + self.company.name + "\n"
        location = "Location: " + self.company.location + "\n"
        contract = "Contract: " + self.contract + "\n"
        description = "Description: " + self.description + "\n"
        salary = "Salary: " + str(self.salary) + "\n"
        
        return title + company + location + contract + description + salary
    
# comp1 = Company("Harnham", "London")
# about = "Design, implement and optimize fraud software solutions Lead multiple workstreams cross Fraud Analytics and Data Science Develop business"
# job = JobOffer("Fraud Analytics Manager", comp1, "Permanent", 120000, about)

# print(job)

# new_about = "Enjoy your job"
# job.update_description(new_about)
# print(job)

def display_text(offer_num):
    print("PLEASE ENTER REQUESTED DATA FOR OFFER ") + str(offer_num)
    title = input("Title: ")
    company = input("Company: ")
    location = input("Location: ")
    contract = input("Contract: ")
    description = input("Description: ")
    salary = input("Salary: ")

def build_job_database():
    print("Welcome to New Job Entry! Let's create our first entry.")
    display_text(1)
    display_text(2)
    return 