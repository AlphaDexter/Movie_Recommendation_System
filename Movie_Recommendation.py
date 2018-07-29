from Genre_Count_matrix import *
from Movie_Genre_User_Relation import *
# from Iterate_ratingsFile import iterate_ratingsFile
from Genre_Count_matrix import *



# Genre_Matrix()
text_file = open('README.txt', 'r')
lines = []


lines = text_file.read().replace(" ", "").replace("\n", "").split("*")

genres = lines[15:33]

genres.insert(18, 'IMAX')
genres.remove("Children's")
genres.insert(3, 'Children')
# print(genres)

movie_hash = iterate_ratingsFile()
# print(movie_hash)
movie_genre_list = movie_genre_list(movie_hash)
# print(movie_genre_list)
correlation_matrix = create_correlation_matrix(genres, movie_genre_list)

requested_genre = ''
recommended_movies = generate_recommendation_points(genres, movie_hash, correlation_matrix, requested_genre)

Od = OrderedDict(sorted(recommended_movies.items(), key=lambda x: x[1]['Recommendation_Points'], reverse=True))

print("Top 10 Recommended movies: ")
print('\n')
for key in Od:
    print(Od[key]['movie_name'], Od[key]['movie_genre'])