#week 4b NLTK wordnet experiments

# https://www.nltk.org/howto/wordnet.html

from nltk.corpus import wordnet as wn

myWordMeanings = wn.synsets('dog')

print(myWordMeanings)

print(wn.synset(myWordMeanings[0].name()).pos())

print(wn.synset(myWordMeanings[0].name()).definition())

print(wn.synset(myWordMeanings[0].name()).lemma_names())

print(wn.synset(myWordMeanings[0].name()).hyponyms())

print(wn.synset(myWordMeanings[0].name()).hypernyms())
