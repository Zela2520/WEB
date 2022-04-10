from django.shortcuts import render

QUESTIONS = [
     {
          "title": f"Title #{i}",
          "text": f"This is the text for question #{i}",
          "number": i,
     } for i in range(10)
]

first_row = {"1": "C/C++", "2": "Python", "3": "SQL"}
second_row = {"1": "Django", "2": "PHP", "3": "JS"}
third_row = {"1": "QT", "2": "Ruby", "3": "Java"}

TAGS = [first_row, second_row, third_row]

names = {"1": "C/C++", "2": "Python", "3": "SQL"}

MEMBERS = ["Mr.Freeman", "Dr.House", "Bender", "Queen Victoria", "V.Pupkin"]

INDEX_CONTENT = [QUESTIONS, TAGS, MEMBERS]

# Create your views here.


def index(request):
     return render(request, "index.html", {"index_content": INDEX_CONTENT})


def ask(request):
     return render(request, "ask.html")


def question(request, i: int):
     return render(request, "question_page.html", {"question": QUESTIONS[i]})
