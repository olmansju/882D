import nltk
from nltk.corpus import inaugural
# nltk.download() uncomment this the first time you run NLTK to make sure you have downloaded what you need

print(inaugural.fileids())

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['american', 'citizen', 'god']
    if w.lower().startswith(target))
cfd.plot()




