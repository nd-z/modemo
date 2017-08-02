from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np
import os.path
#import sys
import scipy.spatial.distance as sd
from skip_thoughts import configuration
from skip_thoughts import encoder_manager
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import cPickle
import time

class BiasAnalyzer(object):
	def __init__(self):
		[lib, con, neu] = cPickle.load(open('sampleData.pkl', 'rb'))

		self.bias_dict = {}

		for tree in lib:
			sentence = tree.get_words()
			self.bias_dict[sentence] = 1

		for tree in con:
			sentence = tree.get_words()
			self.bias_dict[sentence] = -1

		for tree in neu:
			sentence = tree.get_words()
			self.bias_dict[sentence] = 0

		self.encoder = encoder_manager.EncoderManager()
		self.data_encodings = []
		self.data = self.bias_dict.keys()

		#f = open('skipthoughts.pkl', 'rb')
		# right now, we're using a unidirectional skip model;
		# we can try the bidirectional model later
		VOCAB_FILE = "/Users/az/Desktop/projects/modemo/backend/modules/tf/skip_thoughts/pretrained/skip_thoughts_uni_2017_02_02/vocab.txt"
		EMBEDDING_MATRIX_FILE = "/Users/az/Desktop/projects/modemo/backend/modules/tf/skip_thoughts/pretrained/skip_thoughts_uni_2017_02_02/embeddings.npy"
		CHECKPOINT_PATH = "/Users/az/Desktop/projects/modemo/backend/modules/tf/skip_thoughts/pretrained/skip_thoughts_uni_2017_02_02/model.ckpt-501424"

		self.encoder.load_model(configuration.model_config(), vocabulary_file=VOCAB_FILE, embedding_matrix_file=EMBEDDING_MATRIX_FILE, checkpoint_path=CHECKPOINT_PATH)

		self.sentiment = SentimentIntensityAnalyzer()
		#f.close()

	def paragraph_bias(self, sentences):

		# TODO compute aggregate bias score for the whole paragraph
		
		for sentence in sentences:
			#print(sentence)

			temp = self.data
			self.data = [sentence]
			self.data.extend(temp)
			#data.extend(self.bias_dict.keys())

			# process into a vector
			self.data_encodings = self.encoder.encode(self.data)

			# find 5 NN with their NN scores and compute vectors for them as well
			# for each of the sentences in results, get the one with
			# the best semantic similarity
			results = self.get_largest_nn(0)
			#print(results)

			# get compound sentiment score
			sentiment_score = self.sentiment.polarity_scores(sentence)['compound']

			# then use the bias_dict to get its political leaning
			bias_score = self.bias_dict[results[0]]

			# final political bias vector:
			bias_vec = [sentiment_score, results[1], bias_score]

			print(sentence, 'has a bias vector of:')
			print(bias_vec) 

			# and do some math

			# take the NN with the highest yhat val and multiply its NN score
			# with the composite sentiment score AND with the dict value of 
			# its ret_sentence

			# now we have the political bias vector, now what?
			# we could add it to the other vectors in the same paragraph
			# and then in a different method, compute the aggregate thing
			# weighted by paragraph length?

			# after we're done, reset self.data to its original value
			self.data = temp


	# gets the 5 NN and returns the one with the largest semantic similarity
	def get_largest_nn(self, ind, num=5):
  		encoding = self.data_encodings[ind]
  		scores = sd.cdist([encoding], self.data_encodings, "cosine")[0]
  		sorted_ids = np.argsort(scores)
  		#print("Sentence:")
  		#print("", self.data[ind])
  		#print("\nNearest neighbors:")
  		ret = {}
  		for i in range(1, num + 1):
			#print(" %d. %s (%.3f)" % (i, self.data[sorted_ids[i]], scores[sorted_ids[i]]))
			ret[scores[sorted_ids[i]]] = self.data[sorted_ids[i]]

		ret_key = sorted(ret.keys())
		key = ret_key[len(ret_key) - 1]

		#this is a list containing the sentence and its semantic similarity
		# key should be the largest value
		return [ret[key], key]
