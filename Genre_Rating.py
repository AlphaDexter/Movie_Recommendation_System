from Iterate_ratingsFile import *
from Movie_hash_map import *
import csv

# def user_Genre_Rating_Avg:


def compare_movieID():

    # sample_movie_file = "Sample_movies.csv"
    sample_rating_file = "movies.csv"

    # print("k")

    line1_count = 0
    line2_count = 0

    with open(sample_rating_file, 'r', encoding='utf8') as srf:
        print("step 1")

        for row1 in srf:
            line1_count += 1
            if line1_count == 1:
                # print("o")
                continue
            row1_array = row1.split(",")
    return row1_array

            # print(row1_array)

    # with open(sample_movie_file, 'r') as smf:
    #
    #     for row2 in smf:
    #         line2_count += 1
    #         if line2_count == 1:
    #             continue
    #
    #         row2_array = row2.split(",")
    #
    # if row1_array[1] == row2_array[0]:
    #     print("ok")