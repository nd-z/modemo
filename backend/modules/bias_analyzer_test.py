# -*- coding: utf-8 -*-

from tf.bias_analyzer import BiasAnalyzer
from article_crawler import ArticleCrawler
import time
import cPickle

print('if this breaks, remember to add the tf folder to PYTHONPATH and try again')

################ GET WEB CONTENT ###################
url = 'https://www.nytimes.com/2017/08/02/us/politics/trump-immigration.html'
#url='http://www.foxnews.com/politics/2017/08/07/democrats-divided-over-whether-party-should-welcome-pro-life-candidates.html'
crawler = ArticleCrawler()

paragraphs = crawler.url_content(url)

nyt_data = paragraphs
print(nyt_data)
#print(nyt_data)

############## INITIALIZING ANALYZER ###############
print('initializing bias analyzer')
start_time = time.time()
#analyzer = BiasAnalyzer()
analyzer = BiasAnalyzer()
print('done')
print(str(time.time() - start_time))

start_time = time.time()

############## TESTING ARTICLE ANALYSIS ############
totalbias = analyzer.get_article_bias(nyt_data)
print('done')
print(str(time.time() - start_time))
print('total bias index for the entire article')
print(totalbias)

############# SVM TRAINING ##############
'''
analyzer.train_SVM()
print('done')
print(str(time.time() - start_time))
'''