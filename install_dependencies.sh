#!/usr/bin/env bash

RED='\033[0;31m'
GREEN='\033[0;32m'
BLACK='\033[0;30m'

#Make sure Python 2.7 is installed.
function python_check() {
	python_version=$(python --version 2>&1)
	if [[ "$python_version" == *"Python 2.7."* ]]; then
		echo -e "${GREEN}Python Check OK${BLACK}"
	else
		echo -e "${RED}Please install Python 2.7${BLACK}"
		exit 1
	fi
}

echo -e "${GREEN}Installing ML Dependencies...${BLACK}"
pip install --upgrade pip
pip install --upgrade scipy
pip install --upgrade numpy
pip install --upgrade keras
pip install --upgrade nltk
pip install --upgrade gensim
pip install --upgrade vaderSentiment
