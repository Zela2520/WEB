from django.shortcuts import render
import collections
# General information

QUESTIONS = [
     {
          "title": f"Question {i}",
          "text": f"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum {i + 1}",
          "number": i - 1
     } for i in range(1, 11)
]

first_row = {"1": "C/C++", "2": "Python", "3": "SQL"}
second_row = {"1": "Django", "2": "PHP", "3": "JS"}
third_row = {"1": "QT", "2": "Ruby", "3": "Java"}

TAGS = [first_row, second_row, third_row]

MEMBERS = ["Mr.Freeman", "Dr.House", "Bender", "Queen Victoria", "V.Pupkin"]

CONTENT = [QUESTIONS, TAGS, MEMBERS]

# Workers

# Обработчик возвращает строку, состоящую из суммы question.number + 1 (инкрементирует question.number, чтобы было красиво, а не с нуля).
def get_sum_str(i:int, adding_row: int):
    res = i + adding_row
    return str(res)

# картинки я хотел добавить к тайтлу вопроса, чтобы у каждого вопроса была своя картинка
USERS = ["balotelli.png",
         "bob.png",
         "clinok.png",
         "demon_beuty.png",
         "jiza.png",
         "shangs.png",
         "swap.png",
         "zenicu.png",
         "wow.png",
         "mugivary.png"
         ]

# Create your views here.


def index(request):
     return render(request, "index.html", {"index_content": CONTENT, "users": USERS})


def question(request, i: int):
    return render(request, "question_page.html", {"question": QUESTIONS[i], "index_content": CONTENT, "answer_id": get_sum_str(1, QUESTIONS[i].get('number', 0))})


def ask(request):
     return render(request, "ask.html", {"index_content": CONTENT})


def login(request):
     return render(request, "login.html", {"index_content": CONTENT})


def registration(request):
     return render(request, "registration.html", {"index_content": CONTENT})


def settings(request):
     return render(request, "settings.html", {"index_content": CONTENT})


def hot(request):
    return render(request, "hot.html", {"index_content": CONTENT})
