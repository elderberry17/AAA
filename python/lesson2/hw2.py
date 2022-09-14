import string
from typing import List
from nltk.corpus import stopwords

class CountVectorizer:
    def __init__(self):
        self._vocab = []
        self.stopwords = set(stopwords.words('russian'))

    def fit(self, corpus: List[str]) -> None:
        for sentence in corpus:
            tokens = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split()
            for token in tokens:
                if token not in self._vocab and token not in self.stopwords:
                    self._vocab.append(token)
        self._vocab.sort()

    def transform(self, corpus: List[str]) -> List[List[int]]:
        term_matrix = []
        for sentence in corpus:
            sentence_vector = []
            tokens = sentence.translate(str.maketrans('', '', string.punctuation)).lower().split()
            for word in self._vocab:
                if word not in self.stopwords:
                    sentence_vector.append(tokens.count(word))
            term_matrix.append(sentence_vector)
        return term_matrix

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        self.fit(corpus)
        return self.transform(corpus)

    def get_feature_names(self):
        if not self._vocab:
            raise Exception('call fit_transform for start!')
        return self._vocab


corpus = [
    'Crock Pot Pasta! Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients ... Parmesan to taste'
]
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)

# print(vectorizer.get_feature_names())
# Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
#       'fresh', 'ingredients', 'parmesan', 'to', 'taste']

# print(count_matrix)
# Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
#       [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
