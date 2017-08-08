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

		self.blacklist = []

		#f = open('skipthoughts.pkl', 'rb')
		# right now, we're using a unidirectional skip model;
		# we can try the bidirectional model later
		VOCAB_FILE = "/Users/az/Desktop/projects/modemo/backend/modules/tf/skip_thoughts/pretrained/skip_thoughts_uni_2017_02_02/vocab.txt"
		EMBEDDING_MATRIX_FILE = "/Users/az/Desktop/projects/modemo/backend/modules/tf/skip_thoughts/pretrained/skip_thoughts_uni_2017_02_02/embeddings.npy"
		CHECKPOINT_PATH = "/Users/az/Desktop/projects/modemo/backend/modules/tf/skip_thoughts/pretrained/skip_thoughts_uni_2017_02_02/model.ckpt-501424"

		self.encoder.load_model(configuration.model_config(), vocabulary_file=VOCAB_FILE, embedding_matrix_file=EMBEDDING_MATRIX_FILE, checkpoint_path=CHECKPOINT_PATH)

		self.sentiment = SentimentIntensityAnalyzer()
		#f.close()

	# @paragraphs is meant to be the output of the article_crawler
	def get_article_bias(self, paragraphs):
		# for each paragraph, get its bias vector

		total_bias = [0,0,0]
		total_length = 0

		for paragraph in paragraphs:
			total_length += len(paragraph)

		for paragraph in paragraphs:
			p_bias = self.get_paragraph_bias(paragraph)

			# weight it by proportion to total length
			# this is tricky because im not sure what to do with the third entry
			scale = float(len(paragraph))/total_length
			p_bias[0] = scale*p_bias[0]
			p_bias[1] = scale*p_bias[1]
			total_bias[0] += p_bias[0]
			total_bias[1] += p_bias[1]
			total_bias[2] += p_bias[2]

		return total_bias

	# TODO okay so as it stands it looks like it takes around 5-10 minutes to process one article
	# that's way way way too long. it's because im re-encoding the same data w/ each sentence
	# so i think a good optimization would be to see if i can throw all of the sentences in at once
	# and just compute NN for indicies 0 to len(sentences)-1.

	# actually yeah that is much better lol. do this!!
	def get_paragraph_bias(self, sentences):

		# compute aggregate bias score for the whole paragraph
		# format is [lib_score, con_score, neu_score]
		# lib_score and con_score are similarly aggregated, while
		# neu_score is a count of how many neutral sentences are found
		aggregate_score = [0, 0, 0]

		temp = list(self.data)
		self.data = list(sentences)

		self.blacklist = list(sentences)
		bound = len(self.blacklist)+2
		print('bound ' + str(bound))
		self.data.extend(temp)

		self.data_encodings = self.encoder.encode(self.data)

		index = 0
		for sentence in sentences:
			# find 5 NN with their NN scores and compute vectors for them as well
			# for each of the sentences in results, get the one with
			# the best semantic similarity

			# bound ensures that of the NNs found, at least 1 will not be one of the current sentences we're looking for
			results = self.get_largest_nn(index,num=bound)
			#print(results)

			# get compound sentiment score
			sentiment_score = self.sentiment.polarity_scores(sentence)['compound']

			# then use the bias_dict to get its political leaning
			bias_score = self.bias_dict[results[0]]

			# final political bias vector:
			bias_vec = [sentiment_score, results[1], bias_score]

			print(sentence, 'has a bias vector of:')
			print(bias_vec)

			# this computes both the bias direction and intensity
			# ....hopefully lol

			# logic: sentiment multiplied by bias score will give us
			# the correct actual bias; i.e. if a sentence is scored
			# similar to a conservative sentence, but is actually negatively
			# talking about the conservative side, then it should be 
			# treated as a liberal bias --> neg * neg = pos = liberal

			# multiply by bias_vec[1] because the less similar it is to 
			# one of our biased sentences, the less we want it to weigh in
			# the aggregate score
			bias_intensity = bias_vec[1]*bias_vec[2]

			# we may want to threshold the sentiment score
			# because if it's only slightly negative, it might just be
			# due to evaluation inaccuracies

			# this value puts a maximum cap on how much the sentiment score can
			# influence the bias score's magnitude
			# i.e. sentiment value can reduce the weight of the bias score by 
			# at most 2/3
			magnitude_cap = 0.33

			# this value is a threshold for determining when a sentiment score
			# is intense enough to influence the bias direction
			sentiment_thresh = 0.4

			# this value is a threshold that basically says: if the sentence is REALLY
			# similar to one of our dataset sentences, then ignore what the sentiment
			# score is and just continue
			semantic_thresh = 0.75

			if abs(bias_vec[1]) < semantic_thresh:
				if abs(bias_vec[0]) > magnitude_cap:
					if abs(bias_vec[0]) > sentiment_thresh:
						bias_intensity = bias_intensity*bias_vec[0]
					else:
						bias_intensity = bias_intensity*abs(bias_vec[0])

			# rationale: we dont want a sentence's bias index to be drastically reduced just because
			# there isnt much sentiment detected. likewise, we dont want its bias sign flipped just
			# because it's 33% positive or negative, so the threshold for flipping is raised to ensure
			# that only strongly toned sentiments have an impact on the direction of the bias

			# however, if a sentence is deemed to be extremely similar (semantically) to a dataset sentence
			# then completely ignore the sentiment score and move on

			# add to aggregate score
			if bias_intensity > 0:
				aggregate_score[0] += bias_intensity
			elif bias_intensity < 0:
				aggregate_score[1] += bias_intensity
			else:
				aggregate_score[2] += 1

			index += 1

		# after we're done, reset self.data to its original value
		self.data = temp
		self.data_encodings = []
		self.blacklist = []
		print(aggregate_score)
		return aggregate_score


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

		for key in reversed(ret_key):
			target = ret[key]
			if target not in self.blacklist:
				return [target, key]

		print('IF YOURE HERE, SOMETHING REALLY BAD HAPPENED!!')
		#this is a list containing the sentence and its semantic similarity
		# key should be the largest value
		return None
