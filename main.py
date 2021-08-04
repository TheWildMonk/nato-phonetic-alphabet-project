import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

df_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_alphabets():
    user_input = input("Enter a word: ").upper()
    try:
        nato_alphabets = [df_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please!")
        generate_alphabets()
    else:
        print(nato_alphabets)


generate_alphabets()
