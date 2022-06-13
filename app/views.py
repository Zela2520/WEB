from django.shortcuts import render
import collections

QUESTIONS = [
     {
          "title": f"Question {i}",
          "text": f"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum {i + 1}",
          "number": i - 1
     } for i in range(1, 11)
]

first_row = {"1": "C++", "2": "Python", "3": "SQL"}
second_row = {"1": "Django", "2": "PHP", "3": "JS"}
third_row = {"1": "QT", "2": "Ruby", "3": "Java"}

TAGS = [first_row, second_row, third_row]

QUESTIONS_TAGS = ["C++", "Python", "SQL", "Django", "PHP", "JS", "QT", "Ruby", "Java"]

MEMBERS = ["Mr.Freeman", "Dr.House", "Bender", "Queen Victoria", "V.Pupkin"]

CONTENT = [QUESTIONS, TAGS, MEMBERS]


USERS = ["img/balotelli.png",
         "img/bob.png",
         "img/clinok.png",
         "img/demon_beuty.png",
         "img/jiza.png",
         "img/shangs.png",
         "img/swap.png",
         "img/zenicu.png",
         "img/wow.png",
         "img/mugivary.png"
         ]

# Обработчик возвращает строку, состоящую из суммы question.number + 1 (инкрементирует question.number, чтобы было красиво, а не с нуля).
def get_sum_str(i:int, adding_row: int):
    res = i + adding_row
    return str(res)



def get_array_value(i: int, some_list):
    res = some_list[i]
    return str(res)

# Create your views here.


def index(request):
    i = 0
    return render(request, "index.html", {"index_content": CONTENT, "users": USERS, "question_tags": QUESTIONS_TAGS,
                                          "get_picture": get_array_value(i, USERS)})


def question(request, i: int):
    return render(request, "question_page.html", {"question": QUESTIONS[i], "iterator": i, "index_content": CONTENT,
                                                  "answer_id": get_sum_str(1, QUESTIONS[i].get('number', 0)),
                                                  "get_picture": get_array_value(i, USERS), "question_tags": QUESTIONS_TAGS})


def ask(request):
     return render(request, "ask.html", {"index_content": CONTENT})


def login(request):
     return render(request, "login.html", {"index_content": CONTENT})


def registration(request):
     return render(request, "registration.html", {"index_content": CONTENT})


def settings(request):
     return render(request, "settings.html", {"index_content": CONTENT})


def hot(request):
    i = 0
    return render(request, "hot.html", {"index_content": CONTENT, "question_tags": QUESTIONS_TAGS,
                                        "get_picture": get_array_value(i, USERS)})


def tag_listing(request, tag: str):
    i = 0
    return render(request, "tag_listing.html", {"index_content": CONTENT, "cur_tag": tag, "question_tags": QUESTIONS_TAGS,
                                                "get_picture": get_array_value(i, USERS)})


def paginate(request, object_list, per_page=10):
    return page
