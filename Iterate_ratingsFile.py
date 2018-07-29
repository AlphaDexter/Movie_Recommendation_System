import csv
from Movie_hash_map import *
import pickle

def iterate_ratingsFile():
    # movie_hash = movie_hash_map()
    #
    # filename = "ratings.csv"
    # line_count = 0
    # with open(filename, 'r', encoding='utf-8') as ratingfile:
    #     for row in ratingfile:
    #         line_count += 1
    #         if line_count == 1:
    #             continue
    #         row_array = row.replace("\n", "").split(",")
    #         movie_hash[str(row_array[1])]["sum_rating"] = movie_hash[str(row_array[1])].get("sum_rating", 0) + float(row_array[2])
    #         movie_hash[str(row_array[1])]["user_count"] = movie_hash[str(row_array[1])].get("user_count", 0) + 1
    #         movie_hash[str(row_array[1])]["average_rating"] = movie_hash[str(row_array[1])].get("sum_rating") / movie_hash[str(row_array[1])].get("user_count")
    #
    #         if line_count % 1000000 == 0:
    #             print("read {} lines".format(line_count))
    #
    # with open('dict.pickle', 'wb') as handle:
    #     pickle.dump(movie_hash, handle, protocol=pickle.HIGHEST_PROTOCOL)
    with open('dict.pickle', 'rb') as handle:
        movie_hash1 = pickle.load(handle)

    return movie_hash1
