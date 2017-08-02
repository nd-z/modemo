import skipthoughts
import cPickle

model = skipthoughts.load_model()
f = open('skipthoughts.pkl', 'wb')
cPickle.dump(model, f)
f.close()

encoder = skipthoughts.Encoder(model)
f = open('encoder.pkl', 'wb')
cPickle.dump(encoder, f)
f.close()