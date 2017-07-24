![mōdemo](https://i.imgur.com/D8VSbIG.png)

# Project Overview
![Project Overview](https://i.imgur.com/p5ALuCd.png)

# Resources/Information
+ For the ML module
	+ [Skip-thoughts encoder](https://github.com/ryankiros/skip-thoughts)
	+ [Skip-thoughts in Tensorflow](https://github.com/tensorflow/models/tree/master/skip_thoughts)
+ For the Fb API handler (if necessary)
	+ [Extract sorted comments from a post](https://developers.facebook.com/docs/graph-api/reference/v2.10/object/comments)

# Inspiration
Two main ideas utilizing skip-thoughts:
+ Can offer more precise analytics on a given social platform's followers
	+ e.g. Youtube channel can break down the sentiments of their followers per video
+ Can detect emotion (and perhaps bias with some modification) in political articles where there ought to be none
	+ Bonus: Baseline functionality would be to detect when an article is using rage politics to sway opinion
+ More ideas? -Always

## Software Used
+ For the ML module:
	+ Python 2.7
	+ Theano 0.7+
	+ NumPy
	+ SciPy
	+ scikit-learn
	+ NLTK 3
	+ Keras
	+ genism
+ TBD

## Frontend Components
+ React frontend
	+ Facebook API login for personalized analysis
	+ No login for general-purpose bias detection
+ API (using Apiary) to dictate communication between frontend/backend

## Backend Components
+ Backend handler for bridging communication between other backend modules
+ Skip-thought sentiment classification module
+ Facebook crawler to grab personal user content for bias analysis
	+ liked posts/pages
	+ personal posts
	+ TBD
+ Article crawler to grab content for bias analysis in general usage
+ Optional: Django/PostgreSQL to store/compare FB user data from each times that they log in?
	+ Would be a cool way to see how much bias you're getting recently vs. last time you checked
