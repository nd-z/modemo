from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
import cPickle
from nltk import tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class SentimentQuantifier(object):
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()

    def process_article(self, paragraphs):
        paragraph_scores = []
        for paragraph in paragraphs:
            #p_score is just the sum of compound scores for that paragraph
            p_score = self.process_paragraph(paragraph)
            paragraph_scores.extend(p_score)

        sentiment_index = self.aggregate_scores(paragraph_scores)
        return sentiment_index

    def process_paragraph(self, paragraph):
        #aggregate sentiment for paragraph
        p_score = 0
        for sentence in paragraph:
            s_score = self.process_sentence(sentence)
            p_score += s_score

        return p_score

    def process_sentence(self, sentence):
        #get compound score; break up into pos/neg/neu later?
        s_score = self.sia.polarity_scores(sentence)['compound']
        return s_score

    def aggregate_scores(self, compound_scores):
        #TODO aggregate them and formulate a sentiment index

'''
sentences = ['Donald Trump is a mediocre President.', 'The President is neglecting his duties as the leader of this nation.', 'Donald Trump is corrupt!', 'Donald Trump is incompetent and does not care for the wellbeing of this nation.', 'Donald Trump is a misogynist and a horrible person.', 'Subscribe for more news.']

analyzer = SentimentIntensityAnalyzer()

for sentence in sentences:
    vs = analyzer.polarity_scores(sentence)
    print(sentence)
    print(str(vs))
'''
