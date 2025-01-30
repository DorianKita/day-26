import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")


nato_dictonary = {row.letter: row.code for (index, row) in nato.iterrows()}

def generate_phonetic():
    username = input("What is your name:").upper()
    try:
        words = [nato_dictonary[letter] for letter in username]
    except KeyError:
        print("Sorry")
        generate_phonetic()
    else:
        print(words)

generate_phonetic()
