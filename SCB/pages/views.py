from django.shortcuts import render, redirect

# Create your views here.

def home(request):
    context = {
        "articles":[
            {
                "zaglavie":"novini dnes",
                "tqlo":"dnes v 19:00....",
                "date_of_action":"19:00,02.10.20",
                "date_posted":"23:00,01.10.20",
                "city":"Sofia",
                "clicks":0,
            },
            {
                "zaglavie":"novini utre",
                "tqlo":"utre v 12:00....",
                "date_of_action":"12:00,03.10.20",
                "date_posted":"23:00,02.10.20",
                "city":"Sofia",
                "clicks":0,
            },
        ]
        ,"date_today":"02.10.20",
    }
    return redirect('article-list')
    return render(request, 'pages/news.html', context)
