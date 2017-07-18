# Resources/Information
+ For the AI module
	+ [ChatterBot; easily trainable and deployable](https://github.com/gunthercox/ChatterBot)
	+ [ConversationAI repositories](https://github.com/conversationai)
	+ [AI chatbot framework](https://github.com/alfredfrancis/ai-chatbot-framework)
	+ [ConversationAI API example](https://github.com/watson-developer-cloud/conversation-simple)
+ For the ML module
	+ [Skip-thoughts encoder](https://github.com/ryankiros/skip-thoughts)
	+ [Skip-thoughts in Tensorflow](https://github.com/tensorflow/models/tree/master/skip_thoughts)
	+ []

# Inspiration
> Catharsis – n., the discharge of extreme, often negative emotion

People feel a wide range of emotions, with extreme emotions like excitement or misery being just as common as mellow emotions like boredom or uneasiness.

Sometimes you just need to get your thoughts out. You just need to vent, get everything out there for only you to see.

The motivation for this project comes from combining two words:
+ modulate – n., exert a modifying or controlling influence on
+ emotion – n., a natural state of mind deriving from mood

In short, modemo hopes to serve as a helpful, neutral medium through which you can discharge your emotions without harm or insecurity. It does not serve to replace human conversation, but to aid where human conversation cannot.

# Project Overview
TBD: an overarching diagram of the project components

## Software Used
+ Python 2.7
+ Theano 0.7+
+ NumPy
+ SciPy
+ scikit-learn
+ NLTK 3
+ Keras
+ genism
+ BeautifulSoup
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
+ AI module for heuristic-based conversation
+ Webcrawler to find and classify personal user data
+ Django and PostgreSQL DB to store user data for personalized conversation