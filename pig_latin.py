import itertools
from itertools import takewhile
import string
import re
'''
Pig Latin translator

A group of Vatican City police officers are planning a trip to the United States.
Since they only speak Pig Latin, they will need to translate a lot of English phrases.
Write a simple program to perform basic English to Pig Latin translation.

Translation rules:
    1) If a word has no letters, don't translate it.
    2) All punctuation should be preserved.
    3) If the word begins with a capital letter, then the translated word should too.
    4) Separate each word into two parts. The first part is called the "prefix" and extends from the beginning of the word up to, but not including, the first vowel.
        (The letter "y" will be considered a vowel.) The Rest of the word is called the "stem".
    5) The Pig Latin text is formed by reversing the order of the prefix and stem and adding the letters "ay" to the end.
        For example, "sandwich" is composed of "s" + "andwich" + "ay" + "." and would translate to "andwichsay."
    6) If the word contains no consonents, let the prefix be empty and the word be the stem.
        The word ending should be "yay" instead of merely "ay." For example, "I" would be "Iyay".
'''
consonants = "bcdfghjklmnpqrstvwxz" #consonant set
vowels = "aeiouy" #vowel set
punctuation = r"[\w']+|[.,!?;\s]" #symbol set

userWord = re.findall(punctuation, raw_input("Please enter a word:\n")) #takes user string input and splits into list
def translateToPigLatin(wordStr):   #main function to translate a word into Pig Latin
    if(containsAny(consonants+vowels, wordStr) is True): #condition 1: if the word has only numbers or punctuation, returns as is
        return (wordStr)
    elif(containsAny(consonants, wordStr)): #condition 2: if the word is only made up of vowels, adds "yay" to the word
        translatedWord = wordStr + "yay"
        return(translatedWord)
    else: #condition 3: if the word is made up of anything else, splits the word into two parts making the prefix anything before the first vowel and the stem anything after the prefix.
        c = len(list(takewhile(lambda x: x not in vowels, wordStr)))
        translatedWord = wordStr[c:len(wordStr)] + wordStr[0:c] + "ay" #prefix = wordStr[0:c] and stem = wordStr[c:len(wordStr)]
        if(wordStr[0].isupper()): #makes sure if the word was capitalized, it remain capitalized
            return(translatedWord.capitalize())
        else:
            return(translatedWord)

def containsAny(letterSet, aWord): #function to check if a string contains any of the characters defined in a set
    for item in itertools.ifilter(letterSet.__contains__, aWord):
        return False
    return True

i=0 #loops and translates every word of the input string
translatedStr = ""
while (i < userWord.__len__()):
    translatedStr = translatedStr + translateToPigLatin(userWord[i])
    i=i+1

print(translatedStr)

'''Kapila was here~'''
