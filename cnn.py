# TODO docopt

import sys
import csv

import numpy as np
from gensim.models import Word2Vec


class CNN:
    def __init__(self, initial_model=None, vocab=None):
        self.initial_model = initial_model
        self.vocab = vocab

        if not vocab:
            assert initial_model

            self.vocab = list(self.initial_model.vocab)

        self.index = {word: i for (i, word) in enumerate(self.vocab)}

    def tweet_to_indices(self, tweet):
        return [self.index[word] for word in tweet if word in self.vocab]


def parse_tweets(path):
    with open(path) as tweets_file:
        return [row[1:] for row in csv.reader(tweets_file)]


def main():
    try:
        positive_tweets_path = sys.argv[1]
        negative_tweets_path = sys.argv[2]
        embeddings_path = sys.argv[3]
    except IndexError:
        print('Usage: cnn.py <positive_tweets_file> <negative_tweets_file> <word2vec_model>')
        sys.exit(1)

    # Load tweets and vocabulary
    positive_tweets = parse_tweets(positive_tweets_path)
    negative_tweets = parse_tweets(negative_tweets_path)

    cnn = CNN(Word2Vec.load(embeddings_path))
    print(cnn.tweet_to_indices(positive_tweets[0]))
    print(cnn.tweet_to_indices(['laksdfjalskdfjalsdfkjasdlkfjasldfkjasdlfkj',
                                'laksdfjlasdjflkasdjfasldkfjadslkfjaslkdfjasdlkfjaslkdfjadslkjfasldkfj']))

    # Extract initial weights for the embedding layer
    # word2vec_embeddings = Word2Vec.load(embeddings_path)
    # weights = list()
    # for word in vocabulary:
    #    try:
    #        weights.append(word2vec_embeddings[word])
    #    except KeyError:
    #        pass

    ## TODO There might be stuff in here that we do not have embeddings for
    # weights = np.array(map(lambda word: word2vec_embeddings[word], vocabulary))
    # print(weights)


if __name__ == '__main__':
    main()
