from django.shortcuts import render

# Create your views here.

def user_list(request):
        context = {
        }
        return render(request, 'users/user_list.html', context)
