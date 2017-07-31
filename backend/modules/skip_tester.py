from skip-thoughts import skipthoughts
import cPickle

model = skipthoughts.load_model()
# pickle the model so we dont need to download all those files for everyone
f = open('skipthoughts.pkl', 'wb')
cPickle.dump(model, f)
f.close()

encoder = skipthoughts.Encoder(model)
# pickle the encoder as well
f = open('encoder.pkl', 'wb')
cPickle.dump(encoder, f)
f.close()

