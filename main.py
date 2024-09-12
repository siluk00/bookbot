def num_words(text):
    words=text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = dict()

    for i in alphabet:
        count[i]=0
    
    for i in text:
        for j in i:
            if j.isalpha():
                count[j]+=1
    return count

def converttolist(text):
    textconverted = []
    for i in text:
        letter_counted = dict()
        letter_counted["letter"]= i
        letter_counted["number"] = text[i]
        textconverted.append(letter_counted)
    return textconverted

def keyforsort(dict):
    return dict["number"]

def printreport(text, url):
    print("--- Begin report of " + url + " ---")
    print(str(num_words(text)) + " words found in the document")
    letters = converttolist(count_letters(text))
    letters.sort(reverse = True, key=keyforsort)
    for character in letters:
        print("The '" + character["letter"] + "' character was found " + str(character["number"]) + " times")
    print("--- End report ---")


with open("books/frankenstein.txt") as f:
    files = f.read()

printreport(files, "books/frankenstein.txt")