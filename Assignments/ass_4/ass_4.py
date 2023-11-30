# 1. Please complete the following:
#   Your First name and Last Name: Celia Shi
#   Your Student ID: 261175554

# 2. Write your program here: 

import pickle

def read_text(text_path):
    """(str) -> list[str]
    Reads from a file specified by the given path and returns them as a list.
    The strings from the file are seperated by comma.
    If the file cannot be found, a FileNotFoundError will be caught

    Example:
    >>> file_path = "posts.txt"
    >>> read_comments_from_file(file_path)
    [' This is the first comment.', 'Another comment here.', ' And a third comment.']
    """

    try:
        file = open(text_path, "r")
        comments = []

        for line in file:
            line_content = line.split(',')[1]
            comments.append(line_content)
        file.close()

        return comments
    #throws error if invalid path
    except FileNotFoundError:
        print("File does not exist")

def read_pickle(path_to_pickle):
    """(str) -> object
    Reads and returns the content of a pickled file specified by the given path.

    Example:
    >>> pickle_path = "file.pkl"
    >>> read_pickle(pickle_path)
    {'key': 'value', 'number': 42, 'list': [1, 2, 3, 4]}
    """

    file = open(path_to_pickle, "rb")
    content = pickle.load(file)
    file.close()
    return content

def sentiment_frequencies(text, dictionary_word):
    """(str, dict) -> dict
    Calculates the sentiment frequencies of words in the given text based on a sentiment dictionary.

    Examples:
    >>> sentiment_dict = {'positive': ['happy', 'joyful',], 'negative': ['sad', 'terrible']}
    >>> text_example1 = "I feel happy and joyful today."
    >>> sentiment_frequencies(text_example1, sentiment_dict)
    {'positive': 0.33, 'negative': 0.0}

    >>> sentiment_dict = {'positive': ['joyful', 'great'], 'negative': ['sad', 'terrible']}
    >>> text_example2 = "This movie is so sad and terrible."
    >>> sentiment_frequencies(text_example2, sentiment_dict)
    {'positive': 0.0, 'negative': 0.33}

    >>> sentiment_dict = {'positive': ['happy', 'great'], 'negative': ['unhappy', 'terrible']}
    >>> text_example3 = "The weather is great, but I feel a bit unhappy."
    >>> sentiment_frequencies(text_example3, sentiment_dict)
    {'positive': 0.17, 'negative': 0.17}
    """
    word_list = text.split(" ")
    sentiment = dictionary_word.keys()
    frequencies = dict.fromkeys(sentiment, 0)

    #counts the frequency for each sentiment
    for word in word_list:
        for sentiment in dictionary_word:
            if word in dictionary_word[sentiment]:
                frequencies[sentiment] += 1

    #calculates the frequency
    number_of_words = len(word_list)
    for i in frequencies:
        frequencies[i] = round(frequencies[i]/number_of_words, 2)
    
    return frequencies

def compute_polarity(dict_frequency):
    """(dict) -> str
    Traverses all the dictionary keys and returns the first one that has the highest frequencies

    >>> frequency_dict = {'positive': 0.25, 'negative': 0.15, 'neutral': 0.6}
    >>> compute_polarity(frequency_dict)
    'neutral'

    >>> frequency_dict = {'positive': 0.5, 'negative': 0.15, 'neutral': 0.6}
    >>> compute_polarity(frequency_dict)
    'positive'

    >>> frequency_dict = {'positive': 0.1, 'negative': 0.1, 'neutral': 0.05}
    >>> compute_polarity(frequency_dict)
    'positive'
    """

    largest_num = 0
    for key in dict_frequency:
        if dict_frequency[key] > largest_num:
            largest_num = dict_frequency[key]

    #returns the first sentiment that equals the largest number calculated above
    for key in dict_frequency:
        if dict_frequency[key] == largest_num:
            return key

def analyse_text(text_path, dict_path):
    """(str, str) -> list[str]
    Reads the text and pickle file, formatting the text correctly and then
    analysing the sentiment according to the dictionary in the pickle file and computes
    the frequency and polarity and returns a list of according sentiment

    >>> text_file_path = "posts.txt"
    >>> sentiment_dict_path = "sentiment_dictionary.pkl"
    >>> analyse_text(text_file_path, sentiment_dict_path)
    ['POSITIVE', 'NEUTRAL', 'NEGATIVE']

    >>> text_file_path = "posts.txt"
    >>> sentiment_dict_path = "sentiment_dictionary.pkl"
    >>> analyse_text(text_file_path, sentiment_dict_path)
    ['NEGATIVE', 'NEUTRAL', 'POSITIVE']

    >>> text_file_path = "posts.txt"
    >>> sentiment_dict_path = "sentiment_dictionary.pkl"
    >>> analyse_text(text_file_path, sentiment_dict_path)
    ['POSITIVE', 'NEUTRAL', 'NEUTRAL', "NEGATIVE"]    
    """

    content = read_text(text_path)
    sentiment_dict = read_pickle(dict_path)
    stop_words = ["!", ".", ",", "?", ";", "\n"]
    list_polarity = []

    for comment in content:
        converted = comment.lower().strip().split(" ") #formats the comments for analysis

        for word in converted:
            #iterate through each letter and see if its in stop_words
            for letter in word:

                if letter in stop_words:
                    #if it is, replaces the string of the character with an empty string
                    original_word = word
                    word = word.replace(letter, "")
                    #replaces the correct word in the list with the index of the word
                    index = converted.index(original_word)
                    converted[index] = word
        
        formatted_comment = " ".join(converted)
        frequencies = sentiment_frequencies(formatted_comment, sentiment_dict)
        polarity = compute_polarity(frequencies)
        list_polarity.append(polarity)

    return list_polarity

# PART B

class Company():
    '''
    Represents a company with a name and location.

    Instance attributes:
        name (str): The name of the company.
        location (str): The location of the company.

    >>> company1 = Company("TechCo", "CityA")
    >>> print(company1.name)
    'TechCo'
    >>> print(company1.location)
    'CityA'

    >>> company1.update_location("CityB")
    >>> print(company1.location)
    'CityB'

    >>> company2 = Company("SoftCorp", "TownX")
    >>> print(company2.name)
    'SoftCorp'
    >>> print(company2.location)
    'TownX'
    '''
    def __init__(self, name, location):
        ''' (str, str) -> None
        Initializes a new Company instance with the given name and location.
        '''
        self.name = name
        self.location = location

    def update_location(self, new_location):
        ''' (str) -> None
        Updates the location of the company.
        '''
        self.location = new_location

class JobOffer():
    '''
    Represents a job offer with information about the title, company, contract, salary, and description.

    Attributes:
        title (str): The title of the job offer.
        company (Company): The company offering the job.
        contract (str): The type of contract (e.g., full-time, part-time).
        salary (int): The salary associated with the job offer.
        description (str): The description of the job.

    Examples:
    >>> company = Company("TechCo", "CityA")
    >>> job_offer = JobOffer("Software Engineer", company, "Full-time", 90000, "Exciting software development role.")
    >>> print(job_offer.title)
    'Software Engineer'
    >>> print(job_offer.company.name)
    'TechCo'
    >>> print(job_offer.contract)
    'Full-time'
    
    >>> company = Company("TechCo", "CityA")
    >>> job_offer = JobOffer("Software Engineer", company, "Full-time", 90000, "Exciting software development role.")
    >>> job_offer.update_description("New and improved software development role.")
    >>> print(job_offer.description)
    'New and improved software development role.'

    >>> company = Company("TechCo", "CityA")
    >>> job_offer = JobOffer("Software Engineer", company, "Full-time", 90000, "Exciting software development role.")
    >>> print(job_offer)
    Title: Software Engineer
    Company: TechCo
    Location: CityA
    Contract: Full-time
    Description: Exciting software development role.
    Salary: 90000
    '''
    def __init__(self, title, company, contract, salary, description):
        ''' (str, Class, str, int, str) -> None
        Initializes a new JobOffer instance with the given parameters.
        '''
        self.title = title
        self.company = company
        self.contract = contract
        self.salary = salary
        self.description = description

    def update_description(self, new_description):
        ''' (str) -> None
        Updates the description of the job offer.
        '''
        self.description = new_description

    def __str__(self):
        ''' () -> str
        Returns a string representation of the job offer.
        '''
        title = "Title: " + self.title + "\n"
        company = "Company: " + self.company.name + "\n"
        location = "Location: " + self.company.location + "\n"
        contract = "Contract: " + self.contract + "\n"
        description = "Description: " + self.description + "\n"
        salary = "Salary: " + str(self.salary)
        
        return title + company + location + contract + description + salary

def build_job_database():
    ''' () -> None
    Prints prompts to enter information for two job offers, including title, company, location, contract,
    description, and salary. Then, prompts the user to update the description of the first job offer.
    '''

    print("Welcome to New Job Entry! Let's create our first entry.")

    # will do this step twice for the two job offers
    for i in range(1, 3):
        print("PLEASE ENTER REQUESTED DATA FOR OFFER " + str(i))
        title = input("Title: ")
        company = input("Company: ")
        location = input("Location: ")
        contract = input("Contract: ")
        description = input("Description: ")
        salary = input("Salary: ")

        #creates the first JobOffer object
        if i == 1:
            cmp1 = Company(company, location)
            job1 = JobOffer(title, cmp1, contract, int(salary), description)
        #creates the seconf JobOffer object
        else:
            cmp2 = Company(company, location)
            job2 = JobOffer(title, cmp2, contract, int(salary), description)
    
    #modify the first job offer
    print("Employer modified OFFER 1 description!")
    print("PLEASE ENTER THE UPDATED OFFER 1 DESCRIPTION")
    new_description = input("Description: ")
    job1.update_description(new_description) #updates job offer
    print("Find updated OFFER 1 below:")
    print(job1)