![mōdemo](https://i.imgur.com/1PJuYP3.png)

# Project Overview
![Project Overview](https://i.imgur.com/p5ALuCd.png)

# Resources/Information
+ For the ML module
	+ [Sentiment Analyzer](https://github.com/cjhutto/vaderSentiment)
	+ [Ideological Books Corpus](http://cs.umd.edu/~miyyer/ibc/)
	+ [Skip-thoughts (Tensorflow)](https://github.com/tensorflow/models/tree/master/skip_thoughts)
+ For the Fb API handler (if necessary)
	+ [Extract sorted comments from a post](https://developers.facebook.com/docs/graph-api/reference/v2.10/object/comments)
+ For the Article Crawler
	+ [Python Goose](https://github.com/grangier/python-goose)

# Inspiration
Two main ideas utilizing skip-thoughts:
+ Can offer more precise analytics on a given social platform's followers
	+ e.g. Youtube channel can break down the sentiments of their followers per video
+ Can detect emotion (and perhaps bias with some modification) in political articles where there ought to be none
	+ Bonus: Baseline functionality would be to detect when an article is using outrage politics to sway opinion

## Software Used
+ For the ML module (skip-thoughts):
	+ Python 2.7
	+ Theano 0.7+
	+ NumPy
	+ SciPy
	+ scikit-learn
	+ NLTK 3
		+ will need to download some packages via nltk.download() in ipython
	+ Keras
	+ genism
	+ dask
+ For article crawling
	+ Goose

## Frontend Components
+ React frontend
	+ Facebook API login for personalized analysis
	+ No login for general-purpose bias detection
+ API (using Apiary) to dictate communication between frontend/backend

## Backend Components
+ Backend handler for bridging communication between other backend modules
+ Skip-thought sentiment classification module
	+ Theory: Political bias of a sentence is a "vector" with magnitude (degree of bias) and direction (favored side of bias). Currently, there are no popular tools for quantifying political bias, so our way of computing this vector is broken down as follows:
		+ Magnitude is a compound score derived from sentiment analysis, combined with the semantic similary score of a liberal or conservative sentence.
		+ Direction is indicated by 1 or -1.
			+ e.g. [-0.8, 0.45, -1] indicates a strong negative-emotion sentence with a conservative bias (bias predicted at 45%, the -1 indicates conservative; 1 for liberal).
		+ The resulting vector can be scaled (multiplied) by a weight (i.e. length of total paragraph) and combined with other political bias vectors to find the net bias of an article.
+ Facebook crawler to grab personal user content for bias analysis
	+ liked posts/pages
	+ personal posts
	+ TBD
+ Article crawler to grab content for bias analysis in general usage
+ Optional: Django/PostgreSQL to store/compare FB user data from each times that they log in?
	+ Would be a cool way to see how much bias you're getting recently vs. last time you checked
