import pandas as pd
import numpy as np
import requests
import json
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv("final.csv",engine='python')
df2=pd.read_csv("movies.csv",engine='python')
l1=list(df['id'])
l2=list(df2['id'])
l3=list(set(l2)-set(l1))
df_new=pd.DataFrame(columns=['adult','backdrop_path','belongs_to_collection','budget','genres','homepage','id','imdb_id','original_language','original_title','overview','popularity','poster_path','production_companies','production_countries','release_date','revenue','runtime','spoken_languages','status','tagline','title','video','vote_average','vote_count','cast','directors','certification'])
i=0
for id in l3:
    try:
        response= requests.get("https://api.themoviedb.org/3/movie/"+str(id)+"?api_key=735f17efdab039cc1200550a0459ba7c")
        R_dict= json.loads(response.text)
        s=""
        for genre in R_dict['genres']:
            s=s+genre['name']+"|"
        R_dict['genres']=s[:-1]
        k=""
        res=requests.get("https://api.themoviedb.org/3/movie/"+str(id)+"/credits?api_key=735f17efdab039cc1200550a0459ba7c")
        d=json.loads(res.text)
        try:
            counter=0
            for dict in d['cast']:
                if(counter<5):
                    k=k+dict['name']+'|'
                    counter+=1
                else:
                    break
            R_dict['cast']=k[:-1]
            k=''
            for dict in d['crew']:
                if(dict['known_for_department']=='Directing'):
                    k=k+dict['name']+'|'
            R_dict['directors']=k[:-1]
        except:
            print("id:"+str(id))
            R_dict['cast']=""
            R_dict['directors']=""
        s=""
        try:
            res=requests.get("https://api.themoviedb.org/3/movie/"+str(id)+"/release_dates?api_key=735f17efdab039cc1200550a0459ba7c")
            k_dict= json.loads(res.text)
            r=k_dict['results']
            for e in r:
                for keys in e.keys():
                    if(keys!='release_dates'):
                        if(e[keys]=='IN' ):
                            s=e['release_dates'][0]['certification']
        except:
            s=""
        R_dict['certification']=s
        print(R_dict)
        df_new=df_new.append(R_dict,ignore_index=True)
        i+=1
        print(i)
    except:
        print("error :"+str(id))
df_new.to_csv("new.csv")