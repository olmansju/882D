from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from textblob import TextBlob
import readability

def getSomeBooks(howManyBooks, startingAt=1):
    i = howManyBooks
    ii = startingAt
    nothing = 0
    valError = 0
    otherError = 0
    allTheBooks = []
    while i > len(allTheBooks): # 54096 ceiling
        try:
            theText = strip_headers(load_etext(ii)).strip() #load the full text into theText
            theLength = len(theText)
            if len(theText) > 292:
                allTheBooks.append([ii, theText])
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
        ii = ii + 1

    print('all done')
    print (len(allTheBooks))
    return allTheBooks


def prepTextGetScore(theRawTextList):
    gFormatted0 = TextBlob(theRawTextList[1])
    gFormatted1 = gFormatted0.sentences
    gFormatted2 = ' '

    for sentence in gFormatted1:
        gFormatted2 = gFormatted2 + " \n " + str(sentence).replace('\r', ' ').replace('\n', ' ')

    results = readability.getmeasures(gFormatted2, lang='en')

    print("Flesch readability score for book #:", theRawTextList[0], "is", results['readability grades']['FleschReadingEase'])

    return results


def combineResults(books):
    newList = []
    for bookInList in books:
        resultsObject = prepTextGetScore(bookInList)
        newList.append([bookInList[0], resultsObject, bookInList[1]])
    print('all done')
    return newList


g = getSomeBooks(10, 1207)
gg = combineResults(g)  # use this syntax to access readability info: gg[0][1]['readability grades']['Kincaid'] 
