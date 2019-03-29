from django.shortcuts import render

from dappx.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dappx.models import questions, options_selection, surveys


def index(request):
    return render(request,'dappx/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'dappx/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})
@login_required
def resercher_doctor(request):
    return render(request, 'dappx/Resercher_doctor.html')
@login_required
def doctor(request):
    return render(request, 'dappx/doctor.html')
@login_required
def resercher(request):
    return render(request, 'dappx/resercher.html')
@login_required
# def addprofile(request):


def addprofile(request):
    quest = questions.objects.all()
    option = options_selection.objects.all()
    return render(request, 'dappx/add_anketa.html', {"quest": quest, 'option': option})
def create(request):
    if request.method == "POST":
        q = questions()
        q.question_name =  request.POST.get("question_name")
        q.question_type =  request.POST.get("question_type")
        q.save()
    return HttpResponse('Success')
def db_add_profile(request):
    if request.method == "POST":
    # surveys_id = request.POST['']
        # anket_date = request.POST.get("anketdate")
        option_id = request.POST.get("question1")
        quest = questions.objects.all()
        surv = surveys.objects.all()
        if len(surv) == 0:
            survey_id = 1
        else:
            survey_id = surv.last().survey_id+1
        for num_quest in range(2, len(quest)+1):
            option_id = request.POST.get("question"+str(num_quest))
            surv = surveys(survey_id = survey_id, question_id = num_quest, option_id = option_id)
            surv.save()
        # question_answer =request.POST['value']#option_id or row_text_answer_id or date_answer_id
        return HttpResponse("Данные успешно загружены в базу данных")