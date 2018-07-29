import csv
import sys
import shlex

def movie_hash_map():

    movie_filename = "Sample_movies.csv"
    create_movie_hash = {}

    line_count = 0
    with open(movie_filename, 'r', encoding='utf-8') as movie_file:
        for row in csv.reader(movie_file):

            # print(row.decode(errors='ignore'))
            line_count += 1

            if line_count == 1:
                continue
            # if line_count == 23055:
            #     print("movie", row[1])
            #     print(type(row))
            row_array = row
            # print(row_array)

            create_movie_hash[row_array[0]] = {"movie_name": row_array[1], "movie_genre": row_array[2].replace("\n","")}
    # print(create_movie_hash)

    return create_movie_hash