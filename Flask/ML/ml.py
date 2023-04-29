from nltk.corpus import wordnet
import pickle
import requests
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()


class ML:
    def __init__(self):
        self.vec = pickle.loads(open(
            '/home/baadalvm/COP290-Assignment3-photons/Flask/ML/vec_list.pkl', 'rb').read())
        self.feature_names = pickle.loads(open(
            '/home/baadalvm/COP290-Assignment3-photons/Flask/ML/feature.pkl', 'rb').read())
        self.similarity = pickle.loads(open(
            '/home/baadalvm/COP290-Assignment3-photons/Flask/ML/recommendations.pkl', 'rb').read())
        self.r = 0

    def synonym(self, phrase):
        synonyms = []
        for syn in wordnet.synsets(phrase):
            for l in syn.lemmas():
                synonyms.append(l.name())
        return list(set(synonyms))

    def recommend_by_string(self, s):
        s_vec = [0]*len(self.feature_names)
        s = s.lower()
        k = ""
        l = s.split()
        l2 = []
        for i in l:
            l2 = l2+self.synonym(i)
            l2.append(i)
        for i in l2:
            k += ps.stem(i)+" "
        cv = CountVectorizer(max_features=2500, stop_words='english')
        tokens = cv.fit_transform([k]).toarray()[0]
        names = cv.get_feature_names_out()
        for i in names:
            try:
                s_vec[self.feature_names.index(i)] += 1
            except:
                pass
        s_vec = np.array(s_vec).reshape(1, -1)
        similarity = []
        for i in self.vec:
            s = cosine_similarity(i.reshape(1, -1), s_vec)[0][0]
            similarity.append(s)
        s = list(enumerate(similarity))
        s = list(sorted(s, reverse=True, key=lambda x: x[1]))
        l = []
        counter = 0
        for i in s:
            if (i[1] > 0):
                l.append(i[0]+1)
                counter += 1
            if (counter == 20):
                break
        return l

    def recommend_by_vector(self, v):
        s_vec = np.array(v).reshape(1, -1)
        similarity = []
        for i in self.vec:
            s = cosine_similarity(i.reshape(1, -1), s_vec)[0][0]
            similarity.append(s)
        print("E!")
        s = list(enumerate(similarity))
        s = list(sorted(s, reverse=True, key=lambda x: x[1]))
        print("E2")
        l = []
        counter = 0
        for i in s:
            l.append(i[0]+1)
            counter += 1
            if (counter == 20):
                break
        return l

    def update_personilization(self, vec_c, id, type):
        # if type=="Friend":
        #     vec_o=np.divide(vec_o,2,dtype=int)
        #     return np.add(vec_c,vec_o)
        vec_o = self.vec[id-1]
        if type == "Bookmark":
            return np.add(vec_c, vec_o)
        if type == "Movie":
            vec_o = np.multiply(vec_o, 2)
            return np.add(vec_o, vec_c)

