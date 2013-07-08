import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
data = "Try me please! does this work well? hello Mr. T!"
print tokenizer.tokenize(data)
