# Cast-it: Casting Agency Application
Project Description
	This is the capstone project for Full-Stack Udacity Nanodegree. 
	Cast-it models a company that is responsible for creating movies and managing and assigning actors to those movies.
	There are three different roles in the company Casting Assistant, Casting Director, and Executive Producer. 
	Each of them has a different set of permissions to view, add, update and delete movies and actors in the database.

# Project Result
Heroku: 

Localhost: http://127.0.0.1:5000/
## Getting Started

#### Python 3.9.1

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

$ cd YOUR_PROJECT_DIRECTORY_PATH/
$ virtualenv --no-site-packages env
$ source env/bin/activate

#### Installing Dependencies

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

#### Set up Enviornment Variables
run source setup.sh to set the user jwts, auth0 credentials
```bash
source setup.sh
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the main directory first ensure you are working using your created virtual environment.
Each time you open a new terminal session, run: Above setup environment variables and then below.

```bash
flask run --reload
```
The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account
2. Select a unique tenant domain
3. Create a new, single page web application
4. Create a new API
    - in API Settings:
        - Enable RBAC
        - Enable Add Permissions in the Access Token
5. Create new API permissions:
    - `get:actors`
	- `get:movies`
    - `post:actors`
	- `post:movies`
    - `patch:actors`
    - `patch:movies`
	- `delete:actors`
	- `delete:movies`
6. Create new roles for:
    Casting Assistant
	•	Can view actors and movies
	Casting Director 
	•	All permissions a Casting Assistant has and
	•	Add or delete an actor from the database
	•	Modify actors or movies
	Executive Producer
	•	All permissions a Casting Director has and
	•	Add or delete a movie from the database

7. Test your endpoints with [Postman](https://getpostman.com). 
    - Register 3 users - assign the Casting Assistant role to one and Casting Director role to the other.
    - Sign into each account and make note of the JWT.
    - Right-clicking the collection folder for Casting Director,Executive Producer and Casting Assistant, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
    - Run the collection and correct any errors.
8. Final Header Link for my API:
https://dev-fsndnano.us.auth0.com/authorize?audience=casting&response_type=token&client_id=YxJ86LhkIn7crZCd2oMEZpq5wbKxW5LL&redirect_uri=http://localhost:5000

## Running the UnitTescases

dropdb casting_test
createdb casting_test
psql casting_test < casting.pgsql
python test_flaskr.py

### API Reference
Endpoints

GET '/movies'

• Return all movies in the database
• Role Authorized: Assistant, Director, Producer

Example: curl -H "Authorization: Bearer <Token>" http://127.0.0.1:5000/movies
{
    "movies": [
        {
            "release_date": "Tue, 01 Sep 2020 00:00:00 GMT",
            "title": "Elsa Holmes"
        },
        {
            "release_date": "Fri, 01 Aug 2014 00:00:00 GMT",
            "title": "Pursuit of happiness"
        },
        {
            "release_date": "Wed, 01 Sep 2021 00:00:00 GMT",
            "title": "Hobbit2"
        },
        {
            "release_date": "Tue, 01 Jan 2013 00:00:00 GMT",
            "title": "Lord of the Rings"
        },
        {
            "release_date": "Sat, 01 Jan 1972 00:00:00 GMT",
            "title": "The Godfather"
        },
        {
            "release_date": "Sat, 01 Aug 2020 00:00:00 GMT",
            "title": "Batman Begins"
        },
        {
            "release_date": "Sat, 01 Nov 1980 00:00:00 GMT",
            "title": "Raging Bull"
        },
        {
            "release_date": "Sat, 01 Nov 1980 00:00:00 GMT",
            "title": "Raging Bull"
        },
        {
            "release_date": "Sat, 01 Jan 1972 00:00:00 GMT",
            "title": "The Godfather"
        }
    ],
    "success": true
}

GET '/actors'

• Return all actors in the database
• Role Authorized: Assistant, Director, Producer
Example: curl -H "Authorization: Bearer <Token>" http://127.0.0.1:5000/actors
{
    "actors": [
        {
            "age": 36,
            "gender": "male",
            "name": "Frodo Baggins"
        },
        {
            "age": 60,
            "gender": "male",
            "name": "Al Pacino"
        },
        {
            "age": 70,
            "gender": "male",
            "name": "Robert De Niro"
        },
        {
            "age": 70,
            "gender": "male",
            "name": "Robert De Niro"
        },
        {
            "age": 60,
            "gender": "male",
            "name": "Al Pacino"
        },
        {
            "age": 40,
            "gender": "Male",
            "name": "George cooper"
        }
    ],
    "success": true
}

POST '/movies'

• Add a new movie. The new movie must have all four information.
• Role Authorized: Director, Producer
Example: curl -X POST - H '{"Content-Type: application/json", "Authorization: Bearer <TOKEN>}' -d '{"title": "Avengers End Game", "release_date": "2017-10-20"}' http://127.0.0.1:5000/movies
{
    "movies": {
        "release_date": "Sat, 01 Jan 1972 00:00:00 GMT",
        "title": "The Godfather"
    },
    "success": true
}

POST '/actors'

• Add a new actor. The new movie must have all four information.
• Role Authorized: Director, Producer
Example: curl -X POST - H '{"Content-Type: application/json", "Authorization: Bearer <TOKEN>}' -d '{"name": "Timothée Chalamet", "age": 24, "gender": "M", "movie_id": 6}' http://127.0.0.1:5000/actors
{
    "actors": {
        "age": 60,
        "gender": "male",
        "name": "Al Pacino"
    },
    "success": true
}
PATCH '/movies/int:movie_id'

• Update some information of a movie based on a payload.
• Roles authorized : Director
Example: curl http://127.0.0.1:5000/movies/3 -X PATCH -H '{"Content-Type: application/json", "Authorization: Bearer <TOKEN>}' -d '{ "title": "", "release_date": "2020-11-01" }'

{
    "movieid": 4,
    "success": true
}

PATCH '/actors/int:actor_id'

• Update some information of an actor based on a payload.
• Roles authorized : Director
Example: curl -X PATCH - H '{"Content-Type: application/json", "Authorization: Bearer <TOKEN>}' -d '{"name": "", "age": 88, "": "M", "movie_id": }' http://127.0.0.1:5000/actors/3
{
    "actorid": 9,
    "success": true
}

DELETE '/movis/int:movie_id'

• Deletes a movie by id form the url parameter.
• Roles authorized : Executive Producer.
Example: curl -H '{"Content-Type: application/json", "Authorization: Bearer <TOKEN>}' -X DELETE http://127.0.0.1:5000/movies/2
{
    "movieid": 18,
    "success": true
}

DELETE '/actors/int:id'

• Deletes a movie by id form the url parameter.
• Roles authorized : Casting Director, Executive Producer.
Example: curl -H '{"Content-Type: application/json", "Authorization: Bearer <TOKEN>}' -X DELETE http://127.0.0.1:5000/actors/2
{
    "actorid": 18,
    "success": true
}

Error Handling
Errors are returned in the following json format:

{
    'success': False,
    'error': 404,
    'message': 'Resource not found. Input out of range.'
}
The API returns 6 types of errors:

400: bad request
422: unprocessable
404: resource not found
403: forbidden
500: internal server error
AuthError: which mainly results in 401 (unauthorized)

### Author and Acknowledgement


Aman contributed everything in the project.