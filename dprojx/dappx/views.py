from django.shortcuts import render

from dappx.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from dappx.models import questions, options_selection, surveys, date_answers
from django.db.models import F


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

def db_add_profile(request):
    if request.method == "POST":

    # surveys_id = request.POST['']
        quest = questions.objects.all()
        surv = surveys.objects.all()
        date_ans = date_answers.objects.all()

        if len(surv) == 0:
            survey_id = 1
        else:
            survey_id = surv.last().survey_id+1

        for num_quest in range(1, len(quest)+1):
            if quest.values_list('question_type', flat=True).get(pk = num_quest) == 'Date':
                anket_date = request.POST.get("question1_date")
                date_ans = date_answers(date_value = anket_date, question_id = num_quest)
                date_ans.save()
                surv = surveys(survey_id = survey_id, question_id = num_quest, date_answer_id = date_ans.id)
                surv.save()
            else:
                option = options_selection.objects.all()
                option_id = request.POST.get("question"+str(num_quest))
                oid = option.filter(option_id = option_id).filter(question_id = num_quest).only('id')[0]
                surv = surveys(survey_id = survey_id, question_id = num_quest,option = oid)
                surv.save()
        # question_answer =request.POST['value']#option_id or row_text_answer_id or date_answer_id
        return render(request, 'dappx/doctor.html')
#Функуция удаления
def delete(request, id):
    try:
        quest = questions.objects.get(id=id)
        surv = surveys.objects.get(id=id)
        date_ans = date_answers.objects.get(id=id)

        quest.delete()
        surv.delete()
        date_ans.delete()
        return HttpResponseRedirect("resercher_doctor/doctor/addProfile/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")

def saved_ankets(request):
    surv = surveys.objects.all()
    #Select * from surveys left join questions, question это внешный ключ в surveys
    surv_quest = surveys.objects.select_related('question')
    surv_date = surveys.objects.select_related('date_answer')
    surv_opt = surveys.objects.select_related('option')
    surv_count = surv_opt.distinct('survey_id')
    # Добавим в словарь {1: {вопрос1: ответ1, вопрос2: ответ2,...}, 2:{вопрос1: ответ1,...}...}
    dic =  {}
    for surv_row_unique in surv_opt.distinct('survey_id'):
        dic[surv_row_unique.survey_id] = {}
        for surv_row in surv_opt:
            if surv_row_unique.survey_id == surv_row.survey_id:
                q = surv_quest.filter(question_id = surv_row.question_id)[0].question.question_name
                if surv_row.option:
                    ans_sel = surv_row.option.option_name
                    dic[surv_row_unique.survey_id][q] = ans_sel
                elif surv_row.date_answer:
                    da = surv_date.filter(date_answer_id = surv_row.date_answer_id)[0].date_answer.date_value
                    ans_sel = da
                    dic[surv_row_unique.survey_id][q] = ans_sel
    return render(request, 'dappx/saved_ankets.html', {"surv": surv, "surv_quest": surv_quest, "surv_opt":surv_opt, "dic": dic})
