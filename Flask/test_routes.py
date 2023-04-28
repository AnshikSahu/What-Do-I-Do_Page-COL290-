import unittest
from app import app
# print(app.secret_key)
class TestApp(unittest.TestCase):
    def setUp(self):
        self.client =app.test_client()
        self.client.testing =True
    def test_home_page(self):
        response =self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_search_get(self):
        with self.client.session_transaction() as session:
            session['id'] = 5 
        data={'search':"glass jar"}
        response=self.client.post('/search_results',data=data,content_type='multipart/form-data')
        self.assertEqual(response.status_code,200)
    def test_new_user(self):
        with self.client.session_transaction() as session:
            session['id'] = 5 
        data={'Name':'Bijoy','Email':'bijoy@gmail.com','Password':'terrano','User_Name':'Bijoy_Terrano'}
        response=self.client.post('/search_results',data=data,content_type='multipart/form-data')
    def test_login(self):
        with self.client.session_transaction() as session:
            session['id'] = 5 
        data={'User_Name':'AB271202','Password':'asdfghjkl'}
        response=self.client.post('/login/',data=data,content_type='multipart/form-data')
    def test_signup(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_add_reveiw(self):
        with self.client.session_transaction() as session:
            session['id'] = 5 
        data={"fname":"A visual treat","w3review":"This is the best movie that I have ever seen","movie_id":"1"}
        response=self.client.post('/add_review',data=data,content_type='multipart/form-data')
        self.assertEqual(response.status_code,200)
    def test_bookmarks(self):
        with self.client.session_transaction() as session:
            session['id'] = 5
        response=self.client.get('/bookmarks')
        self.assertEqual(response.status_code,200)
    def test_add_bookmarks(self):
        with self.client.session_transaction() as session:
            session['id'] = 5
        data={"movie_id":"1231"}
        response=self.client.post('/add_bookmark',data=data,content_type='multipart/form-data')
        self.assertEqual(response.status_code,200)
    def test_like(self):
        with self.client.session_transaction() as session:
            session['id'] = 5
        data={"userid":"5","movieid":"134","postid":"122","type":"0"}
        response=self.client.post('/likeunlike',data=data,content_type='multipart/form-data')
        self.assertEqual(response.status_code,200)
    def test_unlike(self):
        with self.client.session_transaction() as session:
            session['id'] = 5
        data={"userid":"5","movieid":"134","postid":"122","type":"1"}
        response=self.client.post('/likeunlike',data=data,content_type='multipart/form-data')
        self.assertEqual(response.status_code,200)
    def test_profile_get(self):
        with self.client.session_transaction() as session:
            session['id'] = 5
        response=self.client.get('/profile')
        self.assertEqual(response.status_code,200)
    def test_profile_post(self):
        with self.client.session_transaction() as session:
            session['id'] = 5 
        data={"First_Name":"Adithya","Sur_Name":"Bijoy","Email":"cs1210571@gmail.com","Password":"asdfghjkl","About":"I am an average CS Maggu"}
        response=self.client.post('/profile',data=data,content_type='multipart/form-data')
        self.assertEqual(response.status_code,200)
    def test_movies_get(self):
        with self.client.session_transaction() as session:
            session['id'] = 5 
        data={'movie_id':'123'}
        response=self.client.get('/profile',data=data,content_type='multipart/form-data')
        self.assertEqual(response.status_code,200)
    