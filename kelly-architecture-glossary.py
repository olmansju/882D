import requests
from bs4 import BeautifulSoup


def combineLists(termList, defList):
    # takes two lists and combines them by position
    termDefList = []
    i = 0
    if (len(termList)) == (len(defList)):
        while i < len(termList):
            termDefList.append([termList[i].text, defList[i].text])
            i = i + 1
    else:
        print('Value mismatch between passed lists')
    return termDefList

def cullDTsAndDDs(passedList):
    # takes a list and removes alternative meanings or definitions or empty strings
    newList = []
    for item in passedList:
        if len(item.text) < 1:
            pass
        elif item.text[0] in {'2', '3', '4'}:
            pass
        else:
            newList.append(item)
    return newList


def getWikipediaText(textURL='https://en.wikipedia.org/wiki/Glossary_of_architecture'):
    # takes a URL and returns the text of each paragraph as a string item in a list
    print('Checking URL for elements...')
    html = requests.get(textURL).text
    beautifulFinder = BeautifulSoup(html, 'lxml')
    foundDTs = beautifulFinder.find_all('dt')
    print(len(foundDTs))
    culledDTs = cullDTsAndDDs(foundDTs)
    print(len(culledDTs))
    foundDDs = beautifulFinder.find_all('dd')
    print(len(foundDDs))
    culledDDs = cullDTsAndDDs(foundDDs)
    print(len(culledDDs))
    combinedList = combineLists(culledDTs, culledDDs)
    return combinedList


r = getWikipediaText()
