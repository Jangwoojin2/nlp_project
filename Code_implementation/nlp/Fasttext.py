import fasttext

raw_corpus_fname = 'req_jamo_corpus.txt' # Fill your corpus file
model_fname = 'req_model'      # Fill your model file

skipgram_model = fasttext.cbow(
    raw_corpus_fname,
    model_fname,
    loss = 'hs',        # hinge loss
    ws=1,               # window size
    lr = 0.01,          # learning rate
    dim = 150,          # embedding dimension
    epoch = 5,          # num of epochs
    min_count = 1,     # minimum count of subwords
    encoding = 'utf-8', # input file encoding
    thread = 6          # num of threads
)


