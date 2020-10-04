from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
# Create your views here.

def login_view(request):
        context = {
        }
        return render(request, 'users/user_list.html', context)


def login_view(request):
        context = {
        }
        return render(request, 'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('home')
    else:
        form = UserRegisterForm()
        print("you are registering \n\n")
    context = {'form':form}
    return render(request, 'users/register.html', context)
