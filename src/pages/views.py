from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "this is about me",
        "my_number": 123,
        "my_list": [
            '12', 'abcde', 565678
        ],
        "my_html": "<h1>hi there</h1>"

    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return render(request, "home.html", {})
