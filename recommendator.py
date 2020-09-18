import requests
import json


def get_movies_from_tastedive(name, limit):
    url = "https://tastedive.com/api/similar"
    key = "385310-APIMashu-RQQWJ3WH"
    params = {
        'q': name,
        'type': 'movies',
        'limit': limit,
        'k': key
    }
    res = requests.get(url, params=params)
    movies = json.loads(res.text)
    return movies


def extract_movie_titles(movies):
    return [movie['Name'] for movie in movies]


def get_related_titles(titles):
    combined_list = []
    for title in titles:
        resulting_list = (extract_movie_titles(get_movies_from_tastedive(title)['Similar']['Results']))
        # Make sure the same movie isn't included twice before appending to the combined list
        if len(combined_list) > 0:
            for item in combined_list:
                if item in resulting_list:
                    resulting_list.remove(item)

        combined_list = combined_list + resulting_list
    return combined_list


def get_movie_data(name):
    url = "https://www.omdbapi.com/"
    key = "686a3c9f"
    params = {
        'apikey': key,
        't': name,
        'type': 'movie',
        'r': 'json',
    }
    res = requests.get(url, params=params)
    data = json.loads(res.text)
    return data


def get_movie_rating(data):
    for item in data['Ratings']:
        if item['Source'] == 'Rotten Tomatoes':
            return int(item['Value'][:-1])
    return 0


def get_sorted_recommendations(titles):
    movies = []
    for item in titles:
        movies.append({'title': item, 'rating': get_movie_rating(get_movie_data(item))})
    return sorted(movies, key=lambda movie: (movie['rating'], movie['title']), reverse=True)


# Get information from API
# similar_movies = get_movies_from_tastedive("Black Panther")
# Get a list with similar titles
# print(extract_movie_titles(similar_movies['Similar']['Results']))
# Take a list of movie titles and get a list of similar titles
# movie_list = ["Black Panther", "Captain Marvel"]
# print(get_related_titles(movie_list))
# Get information about a specific movie
# print(get_movie_data("Deadpool 2"))
# print(get_movie_rating(get_movie_data("Deadpool 2")))
# Sort movies by Rotten Tomatoes score
#print(get_sorted_recommendations(['Venom', 'Deadpool 2', 'Black Panther', 'Spiderman', 'Spiderman 2', 'Parasyte']))
# print(get_sorted_recommendations(['Bridesmaids', 'Sherlock Holmes']))