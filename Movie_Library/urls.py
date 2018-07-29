from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^Movie_Library/', views.MovieLibraryView.as_view(), name='MovieLibrary'),
    url(r'^Register/', views.UserFormView.as_view(), name='register'),
    url(r'^Profile/', views.user_account, name='user_account'),
]