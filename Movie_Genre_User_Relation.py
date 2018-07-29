from Genre_Count_matrix import *
from collections import OrderedDict


def take_user_input(genres, requested_genre):
    genre_length = len(genres)
    # print("Preferred genres(separated by spaces)")

    while True:
        user_input = input(str(requested_genre))
        if not user_input:
            break
        # print("Entered genres:", user_input)
        break

    # print("End of while")
    return user_input


def generate_recommendation_points(genres, movie_hash, correlation_matrix, requested_genre):
    # print(movie_hash)
    # print(correlation_matrix)

    recommended_movies = {}
    user_input = take_user_input(genres, requested_genre)
    user_input = user_input.title()
    # print(user_input)

    parsed_user_input = user_input.split(" ")
    # print(parsed_user_input)

    user_genres_len = len(parsed_user_input)

    for key in movie_hash:  # Adding Recommendation points key and assigning 0 initial value
        if 'Recommendation_Points' not in movie_hash[key]:
            movie_hash[key]['Recommendation_Points'] = 0

    for key in movie_hash:  # Adding average rating key for all the movie IDs
        if 'average_rating' not in movie_hash[key]:
            # print('ok')
            movie_hash[key]['average_rating'] = 0

        # print(movie_hash[key]['average_rating'])

        if movie_hash[key]['movie_genre'] == '(no genres listed)':
            movie_hash[key]['movie_genre'] = ''

    # Calculating recommendation points
    for key in movie_hash:

        movie_genre_array = movie_hash[key]['movie_genre']
        movie_genre_list = movie_genre_array.split("|")

        final_sum = 0

        for i in range(len(parsed_user_input)):
            similar_genre_sum = 0
            different_genre_sum = 0
            count = 0

            for j in range(len(movie_genre_list)):

                if movie_genre_list[j] == '':
                    break

                else:
                    if parsed_user_input[i] == movie_genre_list[j]:
                        similar_genre_sum = movie_hash[key]['average_rating']
                        if len(movie_genre_list) != 1:
                            count += 1

                    elif parsed_user_input[i] != movie_genre_list[j]:
                        if count == 1:
                            different_genre_sum += (correlation_matrix[genres.index(parsed_user_input[i])][
                                genres.index(movie_genre_list[j])]) * (movie_hash[key]['average_rating'])
                            # different_genre_sum = different_genre_sum / (len(movie_genre_list) - 1)
                        else:
                            different_genre_sum += (correlation_matrix[genres.index(parsed_user_input[i])][
                                genres.index(movie_genre_list[j])]) * (movie_hash[key]['average_rating'])

                if count == 1:
                    different_genre_sum = different_genre_sum / (len(movie_genre_list) - 1)
                else:
                    different_genre_sum = different_genre_sum / len(movie_genre_list)

            final_sum += (similar_genre_sum + different_genre_sum)

        final_sum = final_sum / len(parsed_user_input)
        movie_hash[key]['Recommendation_Points'] = final_sum

    sorted(movie_hash.items(), key=lambda x: x[1]['Recommendation_Points'], reverse=True)
    # print(len(movie_hash))

    recommendation_count = 0
    # for key in movie_hash:
    # print(Od)
    Od = OrderedDict(sorted(movie_hash.items(), key=lambda x: x[1]['Recommendation_Points'], reverse=True))

    for key, value in Od.items():
        # print(Od[key])
        recommended_movies[key] = Od[key]

        recommendation_count += 1

        if recommendation_count == 10:
            break

    return recommended_movies
