from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from .models import UserProfile


def logout_view(request):
    logout(request)
    return redirect('home')

class UserAccount(View):
    def get(self, request):
        return render(request, 'users/account.html')

    def post(self, request):
        if request.method == "POST":
            profile_image = request.FILES["profile-image"]
            userprofile = request.user.userprofile  
            userprofile.profile_image = profile_image
            userprofile.save()
            return redirect('my-account')
        if request.user.is_authenticated:
            username = request.user.username
            return render(request, 'users/account.html', {'username': username})
        else:
            return redirect('login')
    

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = AuthenticationForm

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return redirect('home')

    def get_success_url(self):
        return redirect('home')


class UserRegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'users/sign-up.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'users/sign-up.html', {'form': form})
