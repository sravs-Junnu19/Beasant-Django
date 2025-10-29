from django.shortcuts import render
from django.http import HttpResponse


# Create your views here
def home(request):
    return HttpResponse("""
        <html>
        <head>
            <title>Home Page</title>
        </head>
        <body style="background-color: lightyellow; text-align: center;">
            <h1 style="font-size: 50px; color: darkblue; margin-top: 100px;">
                My First Web Page in Django
            </h1>
        </body>
        </html>
    """)



def first(request):
    return render(request, "first.html")
