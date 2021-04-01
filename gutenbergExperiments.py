from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

i = 1
nothing = 0
valError = 0
otherError = 0
allTheBooks = []
while i < 54096:
    try:
        theText = strip_headers(load_etext(i)).strip() #load the full text into theText
        theLength = len(theText)
        if len(theText) > 292:
            allTheBooks.append(theText)
            print("one more book in the list, book number:", i, "book total is:", len(allTheBooks))
        else:
            nothing = nothing + 1
            print("nothing here at number:", i)
    except ValueError:
        valError = valError + 1
        print("valueError at book number:", i)
    except:
        otherError = otherError + 1
        print("otherError at book number:", i)
    i = i + 1

print('all done')
print (len(allTheBooks))

#theTextList = theText.split() #make a list object where each word is an item


#print(theText[0]) #print the first character

#print("Moby Dick is " + str(len(theText)) + " characters long.")

#print(theTextList[0]) #print the first item in the list

#print("Moby Dick is " + str(len(theTextList)) + " words long.")

#print("whale appears " + str(whaleCount) + " times in the book")
