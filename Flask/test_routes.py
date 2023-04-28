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
            session['id'] = 1 
        data={'search':"theories"}
        response=self.client.post('/search_results',data=data,content_type='multipart/form-data')
        self.assertEqual(response.status_code,200)
    def test_new_user(self):
        with self.client.session_transaction() as session:
            session['id'] = 1 
        data={'Name':'Bijoy','Email':'bijoy@gmail.com','Password':'terrano','User_Name':'Bijoy_Terrano'}
        response=self.client.post('/search_results',data=data,content_type='multipart/form-data')
    def test_signup(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
    def test_add_reveiw(self):
        with self.client.session_transaction() as session:
            session['id'] = 1 
        data={"fname":"A visual treat","w3review":"This is the best movie that I have ever seen","movie_id":"1"}
        response=self.client.post('/add_review',data=data,content_type='multipart/form-data')
        self.assertEqual(response.status_code,200)
    def test_profile_get(self):
        with self.client.session_transaction() as session:
            session['id'] = 1 
        response=self.client.get('/profile')
        self.assertEqual(response.status_code,200)
    def test_profile_post(self):
        with self.client.session_transaction() as session:
            session['id'] = 1 
        data={"First_Name":"Adithya","Sur_Name":"Bijoy","Email":"cs1210571@gmail.com","Password":"asdfghjkl","About":"I am an average CS Maggu"}
        response=self.client.post('/profile',data=data,content_type='multipart/form-data')
        self.assertEqual(response.status_code,200)
    def test_movies_get(self):
        with self.client.session_transaction() as session:
            session['id'] = 1 
        data={'movie_id':'123'}
        response=self.client.get('/profile',data=data,content_type='multipart/form-data')
        self.assertEqual(response.status_code,200)
    