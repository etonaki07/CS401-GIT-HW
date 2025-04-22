import sys
import json

def read_json(output_file):
    
    # TODO: read the JSON file and return the data
    output_file = sys.argv[1]

    try:
        with open(output_file, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
            print(f"Error: The file '{output_file}' was not found.")
            sys.exit(1)
'''
    This is to read in the json file and return the data. If the file is not found, 
    it will print an error message and exit the program.

'''

def net_profit(data: list[dict]) -> str:
    
    # TODO: movie with the largest net profit of the past 5 years
    movie_name = ""
    highest_profit = 0

    for movie in data:
        if movie['budget'] != "" and movie['grossWorldWide'] != "":

            profit = movie['grossWorldWide'] - movie['budget']
            if profit >= highest_profit:
                highest_profit = profit
                movie_name = movie['Title']

    return movie_name
'''
    This function calculates the net profit of each movie by subtracting the budget from 
    the gross worldwide earnings.

'''

# TODO: add second function to print out interesting statistics about the data
def best_rating(data: list[dict]) -> str:
    highest_rated_movie = ""
    highest_rating = 0.0

    for movie in data:
        if movie['Rating'] != "":
            rating = float(movie['Rating'])
            if rating > highest_rating:
                highest_rating = rating
                highest_rated_movie = movie['Title']
    
    return highest_rated_movie, highest_rating
'''
    This function finds the movie with the highest rating by iterating through the data
    and comparing the ratings. It returns the title of the highest rated movie along with its rating.
'''


# TODO: add third function to print out interesting statistics about the data
def most_frequent_actor(data: list[dict]) -> str:
    actor_count = {}

    for movie in data:
        if "stars" in movie:
            for actor in movie["stars"]:
                actor_count[actor] = actor_count.get(actor, 0) + 1

    most_common_actor = max(actor_count, key=actor_count.get, default=None)
    max_appearances = actor_count.get(most_common_actor, 0)

    return most_common_actor, max_appearances
'''
    This function finds the actor who appeared in the most movies by counting the occurrences
    of each actor in the data. It returns the name of the most common actor along with the number of appearances.
    If no actors are found, it returns None and 0.
  
    Note: The function uses the get method to handle cases where the actor is not found in the dictionary.
'''    

def main():

    if len(sys.argv) < 2:

        print("Error: No command line argument provided. Please provide a file name for a json file to read. i.e. python analyze_data.py data.json")
        sys.exit(1)  # Exit with a non-zero status code to indicate an error

    # Access the command line argument
    output_file = sys.argv[1]

    # TODO: call function to read JSON file and return data
    data = read_json(output_file)
    #print(data)
    

    # TODO: call function to get the movie with the largest net profit of the past 5 years
    net_profit_answer = net_profit(data)

    print( f'Movie with largest net profit: {net_profit_answer}' )

    # TODO: second function to return and print out 
    best_rating_answer, rating_number_answer = best_rating(data)

    print( f'Highest rated movie: {best_rating_answer} with a {rating_number_answer} rating' )
    


    # TODO: third function to return and print out result
    most_common_actor, appearances = most_frequent_actor(data)
    print(f"The actor who appeared in the most movies is {most_common_actor} with {appearances} appearances.")


if __name__ == '__main__':
    main()
