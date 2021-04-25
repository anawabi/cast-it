import os
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actor, Movie
from auth import AuthError, requires_auth

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    # CORS(app)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response

# -------------------------------------------------------------
# Endpoints
# -------------------------------------------------------------

    @app.route('/')
    def index():
        return "Name of movies will list here"


# -----------------------------------
# Movies Endpoints
# -----------------------------------

    # Retrieves list of all movies
    @app.route('/movies', methods=['GET'])
    def get_movies():
        movies = Movie.query.all()
        formatted_movies = [movie.format() for movie in movies]
        return jsonify({
            'success': True,
            'movies': formatted_movies
        })

    #Adds a new movie to DB    
    @app.route('/movies', methods=['POST'])
    def add_movie():
        body = request.get_json()
        title = body['title']
        age = body['age']
        # try:
        entry = Movie(title=title, release_date=release_date)
        entry.insert()
        return jsonify({
            'success': True,
            'movies': entry.format()
        })
        # except:
        #     abort(422)      

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    def update_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        try:
            if movie is None:
                abort(404)
            else:
                body = request.get_json()
                movie.title = body.get('title', None)
                movie.release_date = body.get('release_date', None)
                movie.update()
                return jsonify({
                'success': True,
                'movieid': movie_id
                }),200
        except:
            abort(422)
             


    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    def delete_movie(movie_id):
        movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
        try:
            if movie is None:
                abort(404)
            else:
                movie.delete()
                return jsonify({
                'success': True,
                'movieid': movie_id
                })
        except:
            abort(422)        

# -----------------------------------
# Actors Endpoints
# -----------------------------------

    # Retrives list of all actors

    @app.route('/actors', methods=['GET'])
    def get_actors():
        actors = Actor.query.all()
        formatted_actors = [actor.format() for actor in actors]
        return jsonify({
        'success': True,
        'actors': formatted_actors
        })

    @app.route('/actors', methods=['POST'])
    def add_actor():
        body = request.get_json()
        name = body.get('name', None)
        age = body.get('age', None)
        gender = body.get('gender', None)
        
        try:
            entry = Actor(name=name, age=age, gender=gender)
            entry.insert()
            return jsonify({
                'success': True,
                'movies': entry.format()
            })
        except:
            abort(422)

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    def update_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        try:
            if actor is None:
                abort(404)
            else:
                body = request.get_json()
                actor.name = body.get('name', None)
                actor.age = body.get('age', None)
                actor.gender = body.get('gender', None)
                actor.update()
                return jsonify({
                'success': True,
                'movieid': actor_id
                }),200
        except:
            abort(422)           


    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    def delete_actor(actor_id):
        actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
        try:
            if actor is None:
                abort(404)
            else:
                actor.delete()
                return jsonify({
                'success': True,
                'movieid': actor_id
                })
        except:
            abort(422)        

# after_request decorator to set Access-Control-Allow
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

# Error Handling
    '''
    Example error handling for unprocessable entity
    '''
    @app.errorhandler(AuthError)
    def handle_auth_error(ex):
        response = jsonify(ex.error)
        response.status_code = ex.status_code
        return response

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False, 
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(500)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    @app.errorhandler(401)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Authorization header is expected"
        }), 401

    @app.errorhandler(403)
    def unprocessable(error):
        return jsonify({
            "success": False, 
            "error": 403,
            "message": "forbidden"
        }), 403

    @app.errorhandler(400)
    def unprocessable(error):
        return jsonify({
            "success": False, 
            "error": 400,
            "message": "unprocessable"
        }), 400
    return app