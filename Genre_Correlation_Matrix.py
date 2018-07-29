# import csv
# from Movie_hash_map import *
#
# text_file = open('README.txt', 'r')
# lines = text_file.read().replace("\n", "").split("*")
#
# genres = lines[15:33]
# genre_length = len(genres)
#
# def create_genre_Correlation_matrix(genres, movie_hash):
#     genre_Correlation_matrix = []
#     genre_count = [0]*genre_length
#
#     for i in range(genre_length):
#         genre_array = [0]*genre_length
#         genre_array[i] = None
#
#         genre_Correlation_matrix.append(genre_array)
#
#     for key in movie_hash:
#         genre_for_movie = movie_hash[key]["movie_genre"]
#
#         genre_for_movie = genre_for_movie.split("|")
#
#     genre_for_movie_length = len(genre_for_movie)
#
#     for i in range(genre_for_movie_length):
#
#
#     return genre_Correlation_matrix