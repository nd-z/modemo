import cPickle

class BiasAnalyzer(object):
	def __init__(self):
		self.bias_dict = {'liberal sentence here': 1, 'conservative sentence here': 100}
		# TODO check how long loading the encoder and model takes
		f = open('encoder.pkl', 'rb')
		self.encoder = cPickle.load(f)
		f.close()

		f = open('skipthoughts.pkl', 'rb')
		self.model = cPickle.load(f)
		f.close()

		# TODO load the eval_sick model as well
		self.sick = None

	def paragraph_bias(sentences):
		# TODO for each sentence, compute the evalsick score
		# and then find its most semantically similar biased sentence

		for sentence in sentences:
			# process into a vector
			# find 5 NN with their NN scores and compute vectors for them as well
			# for each of the vectors computed above, find corresponding
			# ret_sentence, yhat pair

			# take the NN with the highest yhat val and multiply its NN score
			# with the composite sentiment score AND with the dict value of 
			# its ret_sentence

			# now we know if its liberal or conservative...what next?

		# TODO after implementing and testing this, try integrating
		# nearest neighbors as well

	#given a sentence, evaluate its semantic similarity with each
	# key in self.bias_dict, and return the bias_dict sentence with
	# the highest similarity score
	def evalsick(sentence):
		highest_yhat = 0
		ret_sentence = None

		for bias_sentence in bias_dict.keys():
			print 'Computing test skipthoughts...'
	        sentence_vec = self.encoder.encode(sentence, verbose=False, use_eos=True)
	        bias_sentence_vec = self.encoder.encode(bias_sentence, verbose=False, use_eos=True)

	        print 'Computing feature combinations...'
	        testF = np.c_[np.abs(sentence_vec - bias_sentence_vec), sentence_vec * bias_sentence_vec]

	        print 'Evaluating...'
	        r = np.arange(1,6)
	        yhat = np.dot(bestlrmodel.predict_proba(testF, verbose=2), r)
	        pr = pearsonr(yhat, scores[2])[0]
	        sr = spearmanr(yhat, scores[2])[0]
	        se = mse(yhat, scores[2])
	        print 'Test Pearson: ' + str(pr)
	        print 'Test Spearman: ' + str(sr)
	        print 'Test MSE: ' + str(se)

	        if yhat > highest_yhat:
	        	highest_yhat = yhat
	        	ret_sentence = bias_sentence

	    return ret_sentence, highest_yhat
