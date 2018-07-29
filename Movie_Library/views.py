from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader, Template
from .models import Movie_Name
from django.views import generic
from django.views.generic import View
# from Movie_Recommendation import *
from django.contrib.auth import authenticate, login
from .forms import UserForm
# import pickle


class MovieLibraryView(generic.ListView):
    template_name = 'Movie_Library.html'
    context_object_name = 'all_movies'

    def get_queryset(self):
        return Movie_Name.objects.all()


def home(request):
    return render(request, 'index.html')


def Movie_Library(request):
    all_movies = Movie_Name.objects.all()
    template = loader.get_template('Movie_Library.html')
    context = {
        'all_movies': all_movies,
    }
    return HttpResponse(template.render(context, request))


def user_account(request):
    return render(request, 'user_account.html')


# User registration
class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    # New user - display blank form
    def get(self, request):
        form = self.form_class(None)

        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Normalised data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']

            user.set_password(password)
            user.save()

            # returns user object if credentials are correct
            user = authenticate(username=username, password=password, email=email)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('user_account')

        return render(request, self.template_name, {'form': form})
