from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='list_users'),
    path('login/', views.login_view, name='login'),
    path('register/',views.register,name='register'),
]
