# Resources/Information
+ For the AI module (we actually probably don't need this anymore)
	+ [ChatterBot; easily trainable and deployable](https://github.com/gunthercox/ChatterBot)
	+ [ConversationAI repositories](https://github.com/conversationai)
	+ [AI chatbot framework](https://github.com/alfredfrancis/ai-chatbot-framework)
	+ [ConversationAI API example](https://github.com/watson-developer-cloud/conversation-simple)
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
+ More ideas?

# Project Overview
TBD: an overarching diagram of the project components

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
+ Facebook login API -> React frontend
+ API to dictate communication between frontend/backend

## Backend Components
+ Facebook API handler to pull personal data for classification, namely
	+ liked posts/pages
	+ personal posts
	+ TBD
+ Skip-thought sentiment classification module
+ Webcrawler to find and classify personal user data
+ Django and PostgreSQL DB to store user data for personalized conversation