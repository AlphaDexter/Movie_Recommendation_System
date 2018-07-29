from django.db import models
# from django.urls import reverse

class Movie_Name(models.Model):
    movie_id = models.CharField(max_length=20)
    movie_name = models.CharField(max_length=200)
    movie_genre = models.CharField(max_length=100)
    movie_year = models.CharField(max_length=10)

    def __str__(self):
        return self.movie_name

class Existing_User_Details(models.Model):
    user_id = models.CharField(max_length=25)
    movie_id = models.CharField(max_length=25)
    user_rating = models.CharField(max_length=10)

    def __str__(self):
        return self.user_id + '-' + self.movie_id + '-' + self.user_rating
