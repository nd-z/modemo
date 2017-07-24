from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
import cPickle

n_instances = 1000
n_train_instances = 8*n_instances/10
#n_test_instances = n_instances - n_train_instances

subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]

train_subj_docs = subj_docs[:n_train_instances]
test_subj_docs = subj_docs[n_train_instances:n_instances]
train_obj_docs = obj_docs[:n_train_instances]
test_obj_docs = obj_docs[n_train_instances:n_instances]
training_docs = train_subj_docs+train_obj_docs

#sentences as a list of unicode words paired to a 'subj' or 'obj' tag in a tuple
print(training_docs)

testing_docs = test_subj_docs+test_obj_docs

#import standard NLTK sentiment analyzer
sentim_analyzer = SentimentAnalyzer()

#track negation words to avoid mischaracterizing sentiments
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
#unigram word features for negation
unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)

#build training and test sets
print(testing_docs)
training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)

trainer = NaiveBayesClassifier.train
print(type(trainer))
print('training classifier')
classifier = sentim_analyzer.train(trainer, training_set)

print('done training; evaluating classifier')
for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
	print('{0}: {1}'.format(key, value))

print('done testing; pickling the classifier')
f = open('sentiment_classifier.pkl', 'wb')
cPickle.dump(classifier, f)