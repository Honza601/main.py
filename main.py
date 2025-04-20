"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jan Čambor
email: jan.cambor@gmail.com
"""

#Zadané texty 
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

line = "-" * 40

#Výběr textu:
text_count = len(TEXTS)

#Registrovaní uživatelé:
usernames = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}

#Přihlášení uživatele:
user = input("Enter your username: ")
password = input("Enter your password: ")

if user in usernames and usernames[user] == password:
    print(line,"\n" "Welcome to the app,", user,"\n" "We have",text_count, "texts to be analyzed.")
    print(line)
else:
    print("unregistered user, terminating the program..")
    quit()

#Výběr textu uživatelem
chosen_text = input("Enter a number btw 1 and " + str(text_count) + " to select: ")
print(line)

if chosen_text.isdigit():
    chosen_text = int(chosen_text)
else:
    print("You can type only numbers")
    quit()
    

if 0 < chosen_text <= text_count:
    text = TEXTS[int(chosen_text)-1]
else:
    print("Choose only btw 1 and " + str(text_count),"!")
    quit()


#Rozbor textu
raw_text = text.split()
clean_text = []

for word in raw_text:
    clean_word = word.strip(",.?!")
    clean_text.append(clean_word)

print("There are",len(clean_text), "words in the selected text.")

title_words = []
upper_words = []
lower_words = []
numbers = []


for word in clean_text:
    if word.istitle():
        title_words.append(word)
    elif word.isupper():
        upper_words.append(word)
    elif word.islower():
        lower_words.append(word)
    elif word.isdigit():
        numbers.append(int(word))


print("There are",len(title_words),"titlecase words.")

print("There are", len(upper_words), "uppercase words.")

print("There are", len(lower_words), "lowercase words.")
    
print("There are", len(numbers), "numeric strings.")    

print("The sum of all the numbers",sum(numbers))
print(line)

print("len".upper() + "|", " occurences".upper(), " |" + "nr.".upper())
print(line)

#Délka slov, graf

word_length = {}

for word in clean_text:
    length = len(word)
    if length in word_length:
        word_length[length] += 1
    else:
        word_length[length] = 1

#Zarovnání podle největší hodnoty 
max_length = max(word_length.values())

for length in sorted(word_length):
    print(f" {length:>2}|{("*" * word_length[length]):<{max_length}} |{word_length[length]:<2}")

