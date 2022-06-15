from django.shortcuts import redirect, render
from django.http import HttpResponse
from paginator import paginate
from django.core.paginator import Paginator
from app.models import *


# Обработчик возвращает строку, состоящую из суммы question.number + 1 (инкрементирует question.number, чтобы было красиво, а не с нуля).
def get_sum_str(i: int, adding_row: int):
    res = i + adding_row
    return str(res)


def get_array_value(i: int, some_list):
    res = some_list[i]
    return str(res)


top_users = Profile.objects.get_top_users(10)

USER = {"is_auth": False}

# Create your views here.


def index(request):
    questions = Question.objects.new()
    page_obj = paginate(questions, request, 10)
    top_tags = Tag.objects.top_tags(10)

    # в блоке ниже группируем данные полученные из БД для их желаемого отображения на странице
    first_row = {"1": top_tags[0], "2": top_tags[1], "3": top_tags[2]}
    second_row = {"1": top_tags[3], "2": top_tags[4], "3": top_tags[5]}
    third_row = {"1": top_tags[6], "2": top_tags[7], "3": top_tags[8]}
    side_panel_tags = [first_row, second_row, third_row]

    content = {
        "questions": page_obj,
        "active_users": top_users,
        "popular_tags": top_tags,
        "side_panel_tags": side_panel_tags,
        "auth": USER['is_auth']
    }

    return render(request, "index.html", content)


def question(request, i: int):
    content = {
        "active_users": top_users,
        "popular_tags": Tag.objects.top_tags(10),
        "auth": USER['is_auth']
    }
    try:
        question = Question.objects.by_id(i)
        answers = paginate(Answer.objects.answer_by_question(i), request, 10)
        content.update({
            "answers": answers,
            "question": question,
        })
    except Exception:
        return render(request, "page_not_found.html", content, status=404)
    return render(request, "question_page.html", content)


def ask(request):
    USER['is_auth'] = True
    content = {
        "active_users": top_users,
        "popular_tags": Tag.objects.top_tags(10),
        "auth": USER['is_auth']
    }
    return render(request, "ask.html", content)


def login(request):
    USER['is_auth'] = True
    content = {
        "active_users": top_users,
        "popular_tags": Tag.objects.top_tags(10),
        "auth": USER['is_auth']
    }
    return render(request, "login.html", content)


def registration(request):
    content = {
        "active_users": top_users,
        "popular_tags": Tag.objects.top_tags(10),
        "auth": False
    }
    return render(request, "registration.html", content)


def settings(request):
    content = {
        "active_users": top_users,
        "popular_tags": Tag.objects.top_tags(10),
        "auth": USER['is_auth']
    }
    return render(request, "setting.html", content)


def logout(request):
    USER['is_auth'] = False
    return index(request)


def hot(request):
    questions = Question.objects.new()
    page_obj = paginate(questions, request, 10)
    top_tags = Tag.objects.top_tags(10)
    content = {
        "questions": page_obj,
        "active_users": top_users,
        "popular_tags": top_tags,
        "auth": USER['is_auth']
    }

    return render(request, "hot.html", content)


def tag_listing(request, tag: str):
    content = {
        "tag": tag,
        "active_users": top_users,
        "popular_tags": Tag.objects.top_tags(10),
        "auth": USER['is_auth']
    }
    try:
        questions = Question.objects.by_tag(tag)
        page_obj = paginate(questions, request, 10)
        content.update({
            "questions": page_obj,
        })
    except Exception:
        return render(request, "page_not_found.html", content, status=404)

    return render(request, "tag_listing.html", content)
