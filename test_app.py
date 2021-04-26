import os
import unittest
import json
import pdb
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie


class CastingTestCase(unittest.TestCase):
    """This class represents the Castingagency test case"""
    
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.testing = True
        # self.database_name = "casting_test"
        self.database_path = 'postgresql://amann:zaq1@WSX@localhost:5432/cast-it'
        setup_db(self.app, self.database_path)
    
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.casting_assistant_auth_header = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijd2d1pSVm5LLWZvLXF0WTh2RGF3UCJ9.eyJpc3MiOiJodHRwczovL2Nhc2hjby51cy5hdXRoMC5jb20vIiwic3ViIjoia0dqb3hpZHdvY2xMd3VTcnVKY1lzbmtydExxSkthZVVAY2xpZW50cyIsImF1ZCI6ImNhc3RpdC1hcGkiLCJpYXQiOjE2MTkzODUyNjcsImV4cCI6MTYxOTQ3MTY2NywiYXpwIjoia0dqb3hpZHdvY2xMd3VTcnVKY1lzbmtydExxSkthZVUiLCJzY29wZSI6ImdldDptb3ZpZXMgZ2V0OmFjdG9ycyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDptb3ZpZXMiLCJnZXQ6YWN0b3JzIl19.ZSp54jZWG1glfgNoPt1yXz6v1w2s9l8hF3tkjN6XqAXIef1EZjATZulFRYr9qt41Ac5iC-6hgaBDoDRWNzoSaTgIqBWrqWnOZMLBrwuaCr5ygT01AP-so2_z5aV6q7bmEr24zhSCuOs9kG-qNfucbWog4Rz4SiPFT92JRJxje3KNgNZH6eZeNkhHR9vCQFVWntKd6o_qNELAmJ5Z29fJ_Iga8bYLWUeXZOd6MoZSsfkIN8WV52htIaSyALyUn2X71TwMd8qovXhNOlTE0PSI9rTZD_V2FgWLHB_1x4GYCXFfxmIjsF1b9jqddc3JpccekmyoaygoX-5bT7N40DnW4g'
        self.casting_director_auth_header = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijd2d1pSVm5LLWZvLXF0WTh2RGF3UCJ9.eyJpc3MiOiJodHRwczovL2Nhc2hjby51cy5hdXRoMC5jb20vIiwic3ViIjoia0dqb3hpZHdvY2xMd3VTcnVKY1lzbmtydExxSkthZVVAY2xpZW50cyIsImF1ZCI6ImNhc3RpdC1hcGkiLCJpYXQiOjE2MTkzODUxNzksImV4cCI6MTYxOTQ3MTU3OSwiYXpwIjoia0dqb3hpZHdvY2xMd3VTcnVKY1lzbmtydExxSkthZVUiLCJzY29wZSI6ImdldDptb3ZpZXMgZ2V0OmFjdG9ycyBwb3N0Om1vdmllcyBwb3N0OmFjdG9ycyBwYXRjaDptb3ZpZXMgcGF0Y2g6YWN0b3JzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOlsiZ2V0Om1vdmllcyIsImdldDphY3RvcnMiLCJwb3N0Om1vdmllcyIsInBvc3Q6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicGF0Y2g6YWN0b3JzIl19.GJ42pqGJhXdt6Po3sGIFW91BzJ5iCMU4tNW-vP2_38QjRnUt68LZ4a5u3z3L2B8JhvRlGkogHg_G5HyK0Z3lQckZrE2XBoS3m6p9V7N_dJ4dQdC_YJgx7Jzjcf8GYefa4OSGX4vLBp-RW2yjtDuPyTsEOXdtsnrNcvdzgBzDegooFEMdPjm1iZboX4jw-bbmo1hJqL6sHIHk6kcLHOYYVpDtKSv-2B4g4HrY1FB7gWcXNBVxBZeHU4VwfzFk6DX2F60KSnhbIUInrGNvogOLozICu-HYHAZ2K7hF1cA61O32FpG1-MudjaOYn2oaHt75lpHYT8tEJ_zoN-Pfw2orHA'
        self.casting_exeproducer_auth_header = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ijd2d1pSVm5LLWZvLXF0WTh2RGF3UCJ9.eyJpc3MiOiJodHRwczovL2Nhc2hjby51cy5hdXRoMC5jb20vIiwic3ViIjoia0dqb3hpZHdvY2xMd3VTcnVKY1lzbmtydExxSkthZVVAY2xpZW50cyIsImF1ZCI6ImNhc3RpdC1hcGkiLCJpYXQiOjE2MTkzODUyMjQsImV4cCI6MTYxOTQ3MTYyNCwiYXpwIjoia0dqb3hpZHdvY2xMd3VTcnVKY1lzbmtydExxSkthZVUiLCJzY29wZSI6ImdldDptb3ZpZXMgZ2V0OmFjdG9ycyBwb3N0Om1vdmllcyBwb3N0OmFjdG9ycyBwYXRjaDptb3ZpZXMgcGF0Y2g6YWN0b3JzIGRlbGV0ZTptb3ZpZXMgZGVsZXRlOmFjdG9ycyIsImd0eSI6ImNsaWVudC1jcmVkZW50aWFscyIsInBlcm1pc3Npb25zIjpbImdldDptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBhdGNoOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJkZWxldGU6YWN0b3JzIl19.YEAXClH2fKn2eJS_Qmh1iBuDwAIKn-6e9Crn4Bvj9ZtcwguZFlr0S3Nbdaf2IAl5V-aRcVGo_2omNTF2taiQwTA6x19-ctgvVVDzC4jUBAF-h631WmG3yioKoSlv-zWnzXZmL5H3By4LbQMxYhEGHpZwRvt3kPmp1qFNs20H0LsW37IQfFHxa6yXNndmEjw_5DsuHOCBANAa-vVR62R1xKR_7lcJbAZx9a6OMmouRMeTsa1u9xH6n9v2C0hgcKbPhXY1WgaAtJjqHrtYnSEmXAzXOzvccub-Ph2GGaoAUbd86wPiQFVe8Mu_JL8t_eU0YY7sT6LlL9u5Oa42BEcxGg'

        self.new_actor = {
            'name': 'Leonardo dicaprio', 
            'age': '44',
            'gender': 'male'
        }
        self.new_movie = {
            'title': 'Inception', 
            'release_date': '2010-11-01'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

  
    '''
     GET /actors and /movies
    '''
    def test_get_actors(self):
        res = self.client().get('/actors', headers = {'Authorization':  'Bearer ' + self.casting_assistant_auth_header})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
 
    def test_failed_get_actors_401(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        print(data)
        
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['code'], 'authorization_header_missing')
        self.assertEqual(data['description'], 'Authorization header is expected.')

    def test_get_movies(self):
        res = self.client().get('/movies', headers = {'Authorization':  'Bearer ' + self.casting_assistant_auth_header})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertTrue(len(data['movies']))

    def test_failed_get_movies(self):
        res = self.client().get('/movies',headers = {'Authorization':  'Bearer ' + self.casting_assistant_auth_header})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])
        self.assertFalse(len(data['movies']) > 25)
    '''
     DELETE /actors and /movies
    '''
    def test_delete_actors(self):
        res = self.client().delete('/actors/14', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header})
        print(res)
        data = json.loads(res.data)
        quest = Actor.query.filter(Actor.id == 14).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['actorid'], 14)

    def test_failed_delete_actors(self):
        res = self.client().delete('/actors/50', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header})
        data = json.loads(res.data)
        quest = Actor.query.filter(Actor.id == 50).one_or_none()

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], 'unprocessable')
        self.assertEqual(data['success'], False)

    def test_delete_movies(self):
        res = self.client().delete('/movies/20', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header})
        data = json.loads(res.data)
        quest = Movie.query.filter(Movie.id == 20).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['movieid'], 20)

    # Using RBAC ROLE testing here ,casting Assistant  doesnt have permission to delete a field.
    def test_failed_delete_movies(self):
        res = self.client().delete('/movies/10', headers = {'Authorization':  'Bearer ' + self.casting_assistant_auth_header})
        data = json.loads(res.data)
        quest = Movie.query.filter(Movie.id == 10).one_or_none()

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')

    '''
     POST /actors and /movies
    '''
    def test_create_actors(self):
        res = self.client().post('/actors', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header}, json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    # def test_post_actor_400(self):
    #     res = self.client().post('/actors', json={'name': '', 'age': '', "gender": ""}, headers={'Authorization':  'Bearer ' + self.casting_director_auth_header})
    #     data = json.loads(res.data)
    #     print(data)

    #     self.assertEqual(res.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Bad Request, pls check your inputs')

    def test_create_movies(self):
        res = self.client().post('/movies', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header}, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    # using RBAC ROLE testing here ,casting assitant doesnt have permission to create new field.
    def test_failed_create_movies_403(self):
        res = self.client().post('/movies', headers = {'Authorization':  'Bearer ' + self.casting_assistant_auth_header}, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')
      

    # '''
    # PATCH /actors and /movies
    # '''

    def test_update_actors(self):
        res = self.client().patch('/actors/16', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header}, json={'name': 'Al Pacino Sr', 'age': 40})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actorid'])

    # using RBAC ROLE testing here ,casting Exceutive producer doesnt have permission to update a field.
    def test_failed_update_actors_403(self):
        res = self.client().patch('/actors/14',headers = {'Authorization':  'Bearer ' + self.casting_exeproducer_auth_header}, json={'name': 'Al Pacino Sr', 'age': 40})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found.')
    
    def test_update_movies(self):
        res = self.client().patch('/movies/4', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header}, json={'release_date': '1999-08-01'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movieid'])

    # Trying to Update a field/row which is not available in DB.
    def test_failed_update_movies_422(self):
        res = self.client().patch('/movies/25', headers = {'Authorization':  'Bearer ' + self.casting_director_auth_header}, json={'release_date': '1999-08-01'})
        data = json.loads(res.data)
        print(data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], 'unprocessable')
        self.assertEqual(data['success'], False)



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
    app.run()