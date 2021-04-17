# based on Kelly's architecture project question

# https://www.flickr.com/services/api/misc.api_keys.html
api_key = u'GET YOUR API KEY AND PASTE IT HERE IN THE QUOTES' 
api_secret = u'PASTE YOUR SECRET HERE IN THE QUOTES'

import requests
from bs4 import BeautifulSoup
import flickrapi


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


def takeListOfTermsAndAddURLforEach(listOfTerms):
    # takes a list of terms and checks each one for images in flickr
    newList = []
    for term in listOfTerms:
        termImageURL = searchFlickrImages(term[0])
        newList.append([term[0], term[1], termImageURL])
    return newList


def searchFlickrImages(term, category='architecture'):
    # takes a term and returns a drawing of it
    flickr = flickrapi.FlickrAPI(api_key, api_secret, format='xmlnode')
    print('searching for term: ' + term + ' in category: ' + category)
    returnedImages = flickr.photos_search(text=term, tags=category, per_page=5, pages=1, extras='url_o', sort='interestingness-desc')
    try:
        g = returnedImages.photos[0].photo[0]
        fl_farm = returnedImages.photos[0].photo[0].attrib['farm']
        fl_server = returnedImages.photos[0].photo[0].attrib['server']
        fl_id = returnedImages.photos[0].photo[0].attrib['id']
        fl_secret = returnedImages.photos[0].photo[0].attrib['secret']
        fl_url = 'http://farm' + fl_farm + '.static.flickr.com/' + fl_server + '/' + fl_id + '_' + fl_secret + '_m.jpg'
        print(fl_url)
        return(fl_url)
    except:
        print('no photo received')
        return ''

def checkListForMissingURLs(passedList):
    # takes a list and checks for missing URLs in the 3rd position
    fullCount = len(passedList)
    count = 0
    for item in passedList:
        if item[2] == '':
            count = count + 1
    if fullCount == count:
        message = '100 percent of terms have an image'
    else:
        percentMissing = round((count/fullCount) * 100, 0)
        message = str(percentMissing) + ' percent of terms missing an image'
    return message


r = getWikipediaText()

rr = takeListOfTermsAndAddURLforEach(r)

print(checkListForMissingURLs(rr))
