from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
<<<<<<< HEAD
    path('', views.user_list, name='list_users'),
    path('login/', views.login_view, name='login'),
=======
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
>>>>>>> a77da727686d4a6b25a679b34e59940ff89634d0
    path('register/',views.register,name='register'),
]
