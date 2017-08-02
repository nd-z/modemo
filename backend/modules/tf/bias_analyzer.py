from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np
import os.path
#import sys
import scipy.spatial.distance as sd
from skip_thoughts import configuration
from skip_thoughts import encoder_manager
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
		#f.close()

	def paragraph_bias(self, sentences):
		# TODO for each sentence, compute the evalsick score
		# and then find its most semantically similar biased sentence

		for sentence in sentences:
			print(sentence)

			temp = self.data
			self.data = [sentence]
			self.data.extend(temp)
			#data.extend(self.bias_dict.keys())

			# process into a vector
			self.data_encodings = self.encoder.encode(self.data)

			# find 5 NN with their NN scores and compute vectors for them as well
			results = self.get_nn(0)
			print(results)
			# for each of the sentences in results, get the one with
			# the best semantic similarity

			# then use the bias_dict to get its political leaning
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

		# TODO after implementing and testing this, try integrating
		# nearest neighbors as well

	#given a sentence, evaluate its semantic similarity with each
	# key in self.bias_dict, and return the bias_dict sentence with
	# the highest similarity score
	# TODO this relied on kiros implementation; modify for current scheme
	'''
	def evalsick(self, sentence):
		highest_yhat = 0
		ret_sentence = None

		for bias_sentence in bias_dict.keys():
			print('Computing test skipthoughts...')
			sentence_vec = self.encoder.encode(sentence)
			bias_sentence_vec = self.encoder.encode(bias_sentence)

			print('Computing feature combinations...')
			testF = np.c_[np.abs(sentence_vec - bias_sentence_vec), sentence_vec * bias_sentence_vec]

			print('Evaluating...')
			r = np.arange(1,6)
			yhat = np.dot(bestlrmodel.predict_proba(testF, verbose=2), r)
			pr = pearsonr(yhat, scores[2])[0]
			sr = spearmanr(yhat, scores[2])[0]
			se = mse(yhat, scores[2])
			# print 'Test Pearson: ' + str(pr)
			# print 'Test Spearman: ' + str(sr)
			# print 'Test MSE: ' + str(se)

			if yhat > highest_yhat:
				highest_yhat = yhat
				ret_sentence = bias_sentence

		return ret_sentence, highest_yhat
	'''

	def get_nn(self, ind, num=5):
  		encoding = self.data_encodings[ind]
  		scores = sd.cdist([encoding], self.data_encodings, "cosine")[0]
  		sorted_ids = np.argsort(scores)
  		print("Sentence:")
  		print("", self.data[ind])
  		print("\nNearest neighbors:")
  		ret = {}
  		for i in range(1, num + 1):
			print(" %d. %s (%.3f)" % (i, self.data[sorted_ids[i]], scores[sorted_ids[i]]))
			ret[self.data[sorted_ids[i]]] = scores[sorted_ids[i]]

		return ret
