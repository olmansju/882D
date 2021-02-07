#week 3 Gutenberg Project in-class experiments

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

theText = strip_headers(load_etext(2701)).strip() #load the full text into theText

theTextList = theText.split() #make a list object where each word is an item

whaleCount = theTextList.count('whale')

print(theText[0]) #print the first character

print("Moby Dick is " + str(len(theText)) + " characters long.")

print(theTextList[0]) #print the first item in the list

print("Moby Dick is " + str(len(theTextList)) + " words long.")

print("whale appears " + str(whaleCount) + " times in the book")