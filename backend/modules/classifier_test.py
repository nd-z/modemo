from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
import cPickle
from nltk import tokenize
#from nltk.sentiment.vader import SentimentIntensityAnalyzer

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentences = ['Donald Trump is a mediocre President.', 'The President is neglecting his duties as the leader of this nation.', 'Donald Trump is corrupt!', 'Donald Trump is incompetent and does not care for the wellbeing of this nation.', 'Donald Trump is a misogynist and a horrible person.']

analyzer = SentimentIntensityAnalyzer()

for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print(sentence)
    print(str(vs))

'''
#the default sentiment analyzer from nltk. not very accurate with these basic sentences
sid = SentimentIntensityAnalyzer()
for sentence in sentences:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print(str(k)+': '+str(ss[k]))
        print('')
'''

#Naive Bayes Classifier...not sure what this does but it might be useful later
'''
f = open('sentiment_classifier.pkl', 'rb')
classifier = cPickle.load(f)

sentim_analyzer = SentimentAnalyzer()

features = sentim_analyzer.apply_features(sentences, labeled=False)
print(features)

print classifier.classify('hello')
'''