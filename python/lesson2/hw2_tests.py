import random
# import unittest

import numpy as np
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer as CV

from hw2 import CountVectorizer


class VectorizerTester:
    def __init__(self):
        self.my_vec = CountVectorizer()
        self.true_vec = CV(stop_words=stopwords.words('russian'))

    def make_corpus(self):
        corpus = []
        n_strings = random.randint(1, 29)
        with open('text.txt', 'r') as f_in:
            lines = f_in.readlines()
            for _ in range(n_strings):
                string_number = random.randint(1, 29)
                corpus.append(lines[string_number])
        return corpus

    def test_term_matrix(self):
        for _ in range(100):
            corpus = self.make_corpus()
            if np.array(self.my_vec.fit_transform(corpus)).all() != self.true_vec.fit_transform(corpus).toarray().all():
                print('fail 1')

            if self.my_vec.get_feature_names() != self.true_vec.get_feature_names():
                print(self.my_vec.get_feature_names())
                print(self.true_vec.get_feature_names())

tester = VectorizerTester()
tester.test_term_matrix()

# how does this goddamn CountVectorizer makes that...