from Movie_hash_map import *
from Iterate_ratingsFile import *

def movie_genre_list(movie_hash):

    movie_genre_listing = {}

    for key in movie_hash:
        movie_genre_listing[key] = movie_hash[key]["movie_genre"]

    for key, value in movie_genre_listing.items():
        if(str(value) == '(no genres listed)'):
            movie_genre_listing[key] = ""
            # print(key)
            # print(movie_genre_listing[key])

    return movie_genre_listing


def create_correlation_matrix(genres, movie_genre_listing):
    genre_length = len(genres)
    genre_count = [0] * genre_length
    # print(genres)

    genre_correlation_matrix = []

    # for i in range(genre_length):
    #     print(genres[i])
    #     print(genres.index(genres[i]))

    for i in range((genre_length)):
        genre_array = [0]*genre_length
        genre_array[i] = None
        genre_correlation_matrix.append(genre_array)


    for key in movie_genre_listing:
        genre_for_movie_len = 0
        genre_for_movie = movie_genre_listing[key]
        # print(genre_for_movie)

        genre_for_movie_list = genre_for_movie.split("|")
        # print(genre_for_movie_list)

        genre_for_movie_len = len(genre_for_movie_list)
        # print(genre_for_movie_len)

        # print(genres)

        for i in range(genre_for_movie_len):
            # print(i)
            # print(str(genre_for_movie_list[i]))

            # if genres[0] == ' Action':
            #     print("okay")
            if genre_for_movie_list[i] != '':
                genre_count[genres.index(genre_for_movie_list[i])] += 1

            for j in range(i+1, genre_for_movie_len):
                if genre_for_movie_list[i] != '':
                    genre_correlation_matrix[genres.index(genre_for_movie_list[i])][genres.index(genre_for_movie_list[j])] += 1
                    genre_correlation_matrix[genres.index(genre_for_movie_list[j])][genres.index(genre_for_movie_list[i])] += 1

    # print(genre_correlation_matrix)
    # print(genre_count)

    for i in range(len(genre_count)):
        for j in range(0,len(genre_count)):
            if genre_correlation_matrix[i][j] != None:
                genre_correlation_matrix[i][j] = genre_correlation_matrix[i][j]/ genre_count[i]

    return genre_correlation_matrix