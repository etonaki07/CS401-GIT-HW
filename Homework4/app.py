from flask import Flask, request, jsonify
import logging
import json



app = Flask(__name__)

# Helper function to retrieve data from the movies.json file
def get_data() -> list[dict]:
    """
    Retrieve the movies dataset and return it as a list of dictionaries.

    Returns:
        data (list[dict]): A list of dictionaries containing the movies dataset.
    """
    with open('movies.json', 'r') as file:
    
        data = json.load(file)

    return data


# TODO: Add a route to return the entire dataset
@app.route('/movies', methods=['GET'])
def get_all_movies() -> jsonify:

    """
    Return the entire dataset of movies.
    """
    logging.debug("Fetching all movies.")

    try:
        movies = get_data()

        return jsonify(movies)

    except Exception as e:
        logging.error(f"Error fetching all movies: {e}")
        return jsonify({"error": "Unable to fetch movies"}), 500

# TODO: Add a route, or modify an existing route, to return the movies that are between a certain release year range
@app.route('/movies/filter', methods=['GET'])
def get_movies_by_year() -> jsonify:

    """
    Return movies filtered by release year range.
    Query Parameters:
        start_year (int): The start year for filtering.
        end_year (int): The end year for filtering.
    """
    try:
        start_year = int(request.args.get('start_year', 2019))
        end_year = int(request.args.get('end_year', 2026))
        logging.debug(f"Filtering movies from {start_year} to {end_year}.")
    except ValueError:
        logging.error("Invalid year range provided.")
        return jsonify({"error": "Invalid year range provided"}), 400

    try:
        movies = get_data()
        filtered_movies = [
            movie for movie in movies
            if (start_year is None or movie['year'] >= start_year) and
               (end_year is None or movie['year'] <= end_year)
        ]

        return jsonify(filtered_movies)

    except Exception as e:
        logging.error(f"Error filtering movies by year: {e}")
        return jsonify({"error": "Invalid input"}), 400


# TODO: Add a route to return a movie if it matches the id
@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie_by_id(movie_id: int) -> jsonify:

    """
    Return a specific movie by its ID.
    Path Parameters:
        movie_id (int): The ID of the movie to retrieve.
    """

    logging.debug(f"Fetching movie with ID: {movie_id}.")

    try:
        movies = get_data()
        movie = next((movie for movie in movies if movie['id'] == movie_id), None)

        if movie:
            return jsonify(movie)
        else:
            return jsonify({"error": "Movie not found"}), 404

    except Exception as e:
        logging.error(f"Error fetching movie by ID: {e}")
        return jsonify({"error": "Invalid input"}), 400

# TODO: Add a route to return the genres for a specific movie
@app.route('/movies/<int:movie_id>/genres', methods=['GET'])
def get_movie_genres(movie_id: int) -> jsonify:

    """
    Return the genres for a specific movie by its ID.
    Path Parameters:
        movie_id (int): The ID of the movie to retrieve genres for.
    """
    logging.debug(f"Fetching genres for movie with ID: {movie_id}.")

    try:
        movies = get_data()
        movie = next((movie for movie in movies if movie['id'] == movie_id), None)

        if movie and 'genres' in movie:
            return jsonify(movie['genres'])
        elif movie:
            return jsonify({"error": "Genres not found for this movie"}), 404
        else:
            return jsonify({"error": "Movie not found"}), 404

    except Exception as e:
        logging.error(f"Error fetching genres for movie: {e}")
        return jsonify({"error": "Invalid input"}), 400

# TODO: Add a route to return a movie if it matches the title
@app.route('/movies/title', methods=['GET'])
def get_movie_by_title() -> jsonify:
    """
    Return a specific movie by its title.
    Query Parameters:
        title (str): The title of the movie to retrieve.
    """
    title = request.args.get('title', type=str)
    logging.debug(f"Fetching movie with title: {title}.")
    try:
        movies = get_data()
        movie = next((movie for movie in movies if movie['title'].lower() == title.lower()), None)

        if movie:
            return jsonify(movie)
        else:
            return jsonify({"error": "Movie not found"}), 404
    except Exception as e:
        logging.error(f"Error fetching movie by title: {e}")
        return jsonify({"error": "Invalid input"}), 400


# the next statement should usually appear at the bottom of a flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
