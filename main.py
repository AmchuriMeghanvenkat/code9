import pandas
data=pandas.read_csv("nato_phonetic_alphabet.csv")
dictionary={row.letter:row.code for (index,row) in data.iterrows()}
# print(dictionary)
word=input("Enter a word: ").upper()
list=[dictionary[letter] for letter in word]
print(list)