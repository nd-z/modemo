# -*- coding: utf-8 -*-

from tf.bias_analyzer import BiasAnalyzer
import time
import cPickle

print('if this breaks, remember to add the tf folder to PYTHONPATH and try again')

#data = ['Donald Trump is a boorish, stupid man.', 'He is unfit to be President, and too dumb to be in the White House.', 'The Democrats are playing a childish game, and would rather see the current healthcare plan continue to cripple America than to pass a new bill.', 'President Trump embraced a proposal on Wednesday to slash legal immigration to the United States in half within a decade by sharply curtailing the ability of American citizens and legal residents to bring family members into the country.', '']

nyt_data = ['President Trump embraced a proposal on Wednesday to slash legal immigration to the United States in half within a decade by sharply curtailing the ability of American citizens and legal residents to bring family members into the country.', 'The plan would enact the most far reaching changes to the system of legal immigration in decades and represents the president’s latest effort to stem the flow of newcomers to the United States.', 'Since taking office, he has barred many visitors from select Muslim majority countries, limited the influx of refugees, increased immigration arrests and pressed to build a wall along the southern border.', 'In asking Congress to curb legal immigration, Mr. Trump intensified a debate about national identity, economic growth, worker fairness and American values that animated his campaign last year.', 'Critics said the proposal would undercut the fundamental vision of the United States as a haven for the poor and huddled masses, while the president and his allies said the country had taken in too many low-skilled immigrants for too long to the detriment of American workers.', '“This legislation will not only restore our competitive edge in the 21st century, but it will restore the sacred bonds of trust between America and its citizens,” Mr. Trump said at a White House event alongside two Republican senators sponsoring the bill.', '“This legislation demonstrates our compassion for struggling American families who deserve an immigration system that puts their needs first and that puts America first.']


print('initializing bias analyzer')
start_time = time.time()
analyzer = BiasAnalyzer()
print('done')
print(str(time.time() - start_time))

analyzer.paragraph_bias(nyt_data)