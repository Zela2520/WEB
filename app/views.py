from django.shortcuts import render

# Список словарей
QUESTIONS = [
     {
          "title": f"Title #{i}",
          "text": f"This is the text for question #{i}",
     } for i in range(10)
]

# Create your views here.


def index(request):
     return render(request, "index.html", {"questions": QUESTIONS})


def ask(request):
     return render(request, "ask.html")
