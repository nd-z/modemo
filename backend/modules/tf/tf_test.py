# Imports.
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import numpy as np
import os.path
import scipy.spatial.distance as sd
from skip_thoughts import configuration
from skip_thoughts import encoder_manager
import cPickle

# Set paths to the model.
VOCAB_FILE = "/Users/az/Desktop/projects/modemo/backend/modules/tf/skip_thoughts/pretrained/skip_thoughts_uni_2017_02_02/vocab.txt"
EMBEDDING_MATRIX_FILE = "/Users/az/Desktop/projects/modemo/backend/modules/tf/skip_thoughts/pretrained/skip_thoughts_uni_2017_02_02/embeddings.npy"
CHECKPOINT_PATH = "/Users/az/Desktop/projects/modemo/backend/modules/tf/skip_thoughts/pretrained/skip_thoughts_uni_2017_02_02/model.ckpt-501424"
# The following directory should contain files rt-polarity.neg and
# rt-polarity.pos.
#MR_DATA_DIR = "/dir/containing/mr/data"

# Set up the encoder. Here we are using a single unidirectional model.
# To use a bidirectional model as well, call load_model() again with
# configuration.model_config(bidirectional_encoder=True) and paths to the
# bidirectional model's files. The encoder will use the concatenation of
# all loaded models.
encoder = encoder_manager.EncoderManager()
encoder.load_model(configuration.model_config(),
                   vocabulary_file=VOCAB_FILE,
                   embedding_matrix_file=EMBEDDING_MATRIX_FILE,
                   checkpoint_path=CHECKPOINT_PATH)

data = ['Donald Trump is a boorish, stupid man.', 'He is unfit to be President, and too dumb to be in the White House.']

[lib, con, neu] = cPickle.load(open('sampleData.pkl', 'rb'))

for tree in lib:
	sentence = tree.get_words()
	data.append(sentence)

for tree in con:
	sentence = tree.get_words()
	data.append(sentence)

for tree in neu:
	sentence = tree.get_words()
	data.append(sentence)

# Generate Skip-Thought Vectors for each sentence in the dataset.
encodings = encoder.encode(data)

# Define a helper function to generate nearest neighbors.
def get_nn(ind, num=5):
  encoding = encodings[ind]
  scores = sd.cdist([encoding], encodings, "cosine")[0]
  sorted_ids = np.argsort(scores)
  print("Sentence:")
  print("", data[ind])
  print("\nNearest neighbors:")
  for i in range(1, num + 1):
    print(" %d. %s (%.3f)" %
          (i, data[sorted_ids[i]], scores[sorted_ids[i]]))

# Compute nearest neighbors of the first sentence in the dataset.
get_nn(0)