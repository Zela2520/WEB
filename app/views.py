from django.shortcuts import render
import collections


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
