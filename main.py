import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

df_dict = {row.letter: row.code for (index, row) in data.iterrows()}

end_program = False
while not end_program:
    user_input = input("Enter a word: ").upper()
    if user_input == "EXIT":
        end_program = True
    else:
        nato_alphabets = [value for each_letter in user_input for key, value in df_dict.items() if each_letter in key]
        print(nato_alphabets)
