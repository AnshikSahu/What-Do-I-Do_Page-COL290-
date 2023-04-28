import pickle
import requests
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
class ML:
    def __init__(self):
        self.vec=pickle.loads(open('/home/baadalvm/COP290-Assignment3-photons/Flask/ML/vec_list.pkl','rb').read())
        self.feature_names=pickle.loads(open('/home/baadalvm/COP290-Assignment3-photons/Flask/ML/feature.pkl','rb').read())
        self.similarity=pickle.loads(open('/home/baadalvm/COP290-Assignment3-photons/Flask/ML/recommendations.pkl','rb').read())
        self.r=0
    def con(self,s):
        a=""
        l=s.split()
        for i in l:
            a=a+ps.stem(i)+" "
        return a
    def recommend_by_string(self,s):
        s_vec=[0]*len(self.feature_names)
        s=self.con(s.lower())
        for i in s.split():
            try:
                s_vec[self.feature_names.index(i)]+=1
            except:
                pass   
        s_vec=np.array(s_vec).reshape(1,-1)
        similarity=[]
        for i in self.vec:
            s=cosine_similarity(i.reshape(1,-1),s_vec)[0][0]
            similarity.append(s)
        s=list(enumerate(similarity))
        s=list(sorted(s,reverse=True,key=lambda x:x[1]))
        s=s[1:21]
        l=[]
        for i in s:
            l.append(i[0])
        return l
    def recommend_by_vector(self,v):
        s_vec=np.array(v).reshape(1,-1)
        similarity=[]
        for i in self.vec:
            s=cosine_similarity(i.reshape(1,-1),s_vec)[0][0]
            similarity.append(s)
        s=list(enumerate(similarity))
        s=list(sorted(s,reverse=True,key=lambda x:x[1]))
        s=s[1:21]
        l=[]
        for i in s:
            l.append(i[0])
        return l
    def update_personilization(self,vec_c,id,type):
        # if type=="Friend":
        #     vec_o=np.divide(vec_o,2,dtype=int)
        #     return np.add(vec_c,vec_o)
        vec_o=self.vec[id]
        if type=="Bookmark":
            return np.add(vec_c,vec_o)
        if type=="Movie":
            vec_o=np.multiply(vec_o,2)
            return np.add(vec_o,vec_c)
    def sentiment(self,s):
        print("API")
        url = "https://api.apilayer.com/sentiment/analysis"
        s=s.replace(" ","%20")
        payload = s.encode("utf-8")
        headers= {
        "apikey": "iOMAkbUfYHMxxXE00rY5k3phtiQV0tIU"}
        response = requests.request("POST", url, headers=headers, data = payload)
        result = json.loads(response.text)
        if(result['sentiment']=="negative"):
            print("-1")
            return -1
        if(result['sentiment']=="positive"):
            print("1")
            return 1
        print("0")
        return 0
    def related_to_movie(self,id):
        return self.similarity[id]