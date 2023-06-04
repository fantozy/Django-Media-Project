from django.urls import path
from .views import UserLoginView, UserRegisterView, UserAccount, logout_view

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('my-account/', UserAccount.as_view(), name='my-account'),
    path('logout/', logout_view, name='logout'),
]
