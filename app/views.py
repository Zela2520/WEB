from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from app.models import *


from django.contrib import auth
from app.forms import LoginForm,  QuestionForm, SettingsForm, SignUpForm, AnswerForm
from django.core.cache import cache
from askme_zela.settings import LOGIN_URL

from django.contrib.auth.decorators import login_required


# Обработчик возвращает строку, состоящую из суммы question.number + 1 (инкрементирует question.number, чтобы было красиво, а не с нуля).


def get_sum_str(i: int, adding_row: int):
    res = i + adding_row
    return str(res)


def get_array_value(i: int, some_list):
    res = some_list[i]
    return str(res)


top_users = Profile.objects.get_top_users(10)

# Create your views here.

USER = {"is_auth": False}

def index(request):
    questions = Question.objects.new()
    paginator = Paginator(questions, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    top_tags = Tag.objects.top_tags(10)

    # в блоке ниже группируем данные полученные из БД для их желаемого отображения на странице
    first_row = {"1": top_tags[0], "2": top_tags[1], "3": top_tags[2]}
    second_row = {"1": top_tags[3], "2": top_tags[4], "3": top_tags[5]}
    third_row = {"1": top_tags[6], "2": top_tags[7], "3": top_tags[8]}
    side_panel_tags = [first_row, second_row, third_row]

    content = {
        "context": page_obj,
        "active_users": top_users,
        "popular_tags": top_tags,
        "side_panel_tags": side_panel_tags,
        "auth": USER['is_auth']
    }

    return render(request, "index.html", content)


def question(request, i: int):
    top_tags = Tag.objects.top_tags(10)
    first_row = {"1": top_tags[0], "2": top_tags[1], "3": top_tags[2]}
    second_row = {"1": top_tags[3], "2": top_tags[4], "3": top_tags[5]}
    third_row = {"1": top_tags[6], "2": top_tags[7], "3": top_tags[8]}
    side_panel_tags = [first_row, second_row, third_row]

    content = {
        "active_users": top_users,
        "popular_tags": Tag.objects.top_tags(10),
        "side_panel_tags": side_panel_tags,
    }

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect(f'{LOGIN_URL}?continue={request.path}')
        else:
            form = AnswerForm(data=request.POST)
            if (form.is_valid):
                ans = form.save(commit=False)
                profile = Profile.objects.get(id=request.user.id)
                question = Question.objects.get(id=i)
                ans.profile = profile
                ans.question = question
                ans.save()

                answers = Paginator(Answer.objects.answer_by_question(i), 10)
                return redirect(f"{request.path}?page={answers.num_pages}#{ans.id}")

    if request.method == "GET":
        try:
            question = Question.objects.by_id(i)
            answers = Answer.objects.answer_by_question(i)
            paginator = Paginator(answers, 5)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            form = AnswerForm()

            content.update({
                "context": page_obj,
                "question": question,
                "form": form
            })
        except Exception:
            return render(request, "page_not_found.html", content, status=404)

    return render(request, "question_page.html", content)


def hot(request):
    questions = Question.objects.hot()
    paginator = Paginator(questions, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    top_tags = Tag.objects.top_tags(10)
    first_row = {"1": top_tags[0], "2": top_tags[1], "3": top_tags[2]}
    second_row = {"1": top_tags[3], "2": top_tags[4], "3": top_tags[5]}
    third_row = {"1": top_tags[6], "2": top_tags[7], "3": top_tags[8]}
    side_panel_tags = [first_row, second_row, third_row]

    content = {
        "context": page_obj,
        "active_users": top_users,
        "side_panel_tags": side_panel_tags,
        "popular_tags": top_tags,
        "auth": USER['is_auth']
    }

    return render(request, "hot.html", content)


def tag_listing(request, tag: str):
    top_tags = Tag.objects.top_tags(10)
    first_row = {"1": top_tags[0], "2": top_tags[1], "3": top_tags[2]}
    second_row = {"1": top_tags[3], "2": top_tags[4], "3": top_tags[5]}
    third_row = {"1": top_tags[6], "2": top_tags[7], "3": top_tags[8]}
    side_panel_tags = [first_row, second_row, third_row]

    content = {
        "tag": tag,
        "active_users": top_users,
        "side_panel_tags": side_panel_tags,
        "popular_tags": Tag.objects.top_tags(10),
        "auth": USER['is_auth']
    }
    try:
        questions = Question.objects.by_tag(tag)
        paginator = Paginator(questions, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        content.update({
            "context": page_obj,
        })
    except Exception:
        return render(request, "page_not_found.html", content, status=404)

    return render(request, "tag_listing.html", content)


@login_required(login_url="login", redirect_field_name="continue")
def ask(request):
    top_tags = Tag.objects.top_tags(10)
    first_row = {"1": top_tags[0], "2": top_tags[1], "3": top_tags[2]}
    second_row = {"1": top_tags[3], "2": top_tags[4], "3": top_tags[5]}
    third_row = {"1": top_tags[6], "2": top_tags[7], "3": top_tags[8]}
    side_panel_tags = [first_row, second_row, third_row]

    if request.method == "GET":
        form = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(data=request.POST)
        if form.is_valid():
            profile = Profile.objects.get(id=request.user.id)
            question = form.save(profile)
            return redirect(f"../question/{question.id}")

    content = {
        "active_users": top_users,
        "side_panel_tags": side_panel_tags,
        "popular_tags": Tag.objects.top_tags(10),
        "form": form
    }

    return render(request, "ask.html", content)


def login(request):
    next = request.GET.get("continue")

    if not next:
        next = "index"

    if request.user.is_authenticated:
        return redirect(next)
    if request.method == "GET":
        form = LoginForm()
        cache.set("continue", next)
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = auth.authenticate(request, **form.cleaned_data)

            if user:
                auth.login(request, user)

                next_url = cache.get('continue')
                if not next_url:
                    next_url = "index"

                cache.delete('continue')
                return redirect(next_url)
            else:
                form.add_error(None, "Invalid password or login!")
                form.add_error('username', "")
                form.add_error('password', "")

    top_tags = Tag.objects.top_tags(10)
    first_row = {"1": top_tags[0], "2": top_tags[1], "3": top_tags[2]}
    second_row = {"1": top_tags[3], "2": top_tags[4], "3": top_tags[5]}
    third_row = {"1": top_tags[6], "2": top_tags[7], "3": top_tags[8]}
    side_panel_tags = [first_row, second_row, third_row]
    content = {
        "active_users": top_users,
        "side_panel_tags": side_panel_tags,
        "popular_tags": Tag.objects.top_tags(10),
        "form": form
    }
    return render(request, "login.html", content)


def registration(request):
    if request.user.is_authenticated:
        return redirect("index")
    if request.method == "GET":
        form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            profile = form.save()
            auth.login(request, profile.user)
            return redirect("index")

    top_tags = Tag.objects.top_tags(10)
    first_row = {"1": top_tags[0], "2": top_tags[1], "3": top_tags[2]}
    second_row = {"1": top_tags[3], "2": top_tags[4], "3": top_tags[5]}
    third_row = {"1": top_tags[6], "2": top_tags[7], "3": top_tags[8]}
    side_panel_tags = [first_row, second_row, third_row]
    content = {
        "active_users": top_users,
        "side_panel_tags": side_panel_tags,
        "popular_tags": Tag.objects.top_tags(10),
        "auth": False
    }
    return render(request, "registration.html", content)


@login_required(login_url="login", redirect_field_name="continue")
def settings(request):
    user = User.objects.get(id=request.user.id)
    if request.method == "GET":
        form = SettingsForm(instance=user)
    if request.method == "POST":
        form = SettingsForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("settings")

    top_tags = Tag.objects.top_tags(10)
    first_row = {"1": top_tags[0], "2": top_tags[1], "3": top_tags[2]}
    second_row = {"1": top_tags[3], "2": top_tags[4], "3": top_tags[5]}
    third_row = {"1": top_tags[6], "2": top_tags[7], "3": top_tags[8]}
    side_panel_tags = [first_row, second_row, third_row]
    content = {
        "active_users": top_users,
        "side_panel_tags": side_panel_tags,
        "popular_tags": Tag.objects.top_tags(10),
        "form": form
    }
    return render(request, "settings.html", content)


def logout(request):
    auth.logout(request)
    return redirect(request.META.get('HTTP_REFERER'))
