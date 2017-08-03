from tf.bias_analyzer import BiasAnalyzer
import time
import cPickle

print('if this breaks, remember to add the tf folder to PYTHONPATH and try again')

data = ['Donald Trump is a boorish, stupid man.', 'He is unfit to be President, and too dumb to be in the White House.', 'The Democrats are playing a childish game, and would rather see the current healthcare plan continue to cripple America than to pass a new bill.']

print('initializing bias analyzer')
start_time = time.time()
analyzer = BiasAnalyzer()
print('done')
print(str(time.time() - start_time))

analyzer.paragraph_bias(data)