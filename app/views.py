from django.shortcuts import render

# General information

QUESTIONS = [
     {
          "title": f"Question {i + 1}",
          "text": f"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum {i + 1}",
          "number": i,
     } for i in range(10)
]

first_row = {"1": "C/C++", "2": "Python", "3": "SQL"}
second_row = {"1": "Django", "2": "PHP", "3": "JS"}
third_row = {"1": "QT", "2": "Ruby", "3": "Java"}

TAGS = [first_row, second_row, third_row]

names = {"1": "C/C++", "2": "Python", "3": "SQL"}

MEMBERS = ["Mr.Freeman", "Dr.House", "Bender", "Queen Victoria", "V.Pupkin"]

CONTENT = [QUESTIONS, TAGS, MEMBERS]

# Create your views here.


def index(request):
     return render(request, "index.html", {"index_content": CONTENT})


def ask(request):
     return render(request, "ask.html", {"index_content": CONTENT})


def login(request):
     return render(request, "login.html", {"index_content": CONTENT})


def registration(request):
     return render(request, "registration.html", {"index_content": CONTENT})


def settings(request):
     return render(request, "settings.html", {"index_content": CONTENT})


def tag_listing(request):
     return render(request, "tag_listing.html", {"index_content": CONTENT})


def question(request, i: int):
     return render(request, "question_page.html", {"question": QUESTIONS[i]})
