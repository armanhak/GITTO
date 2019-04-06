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
    surv = surveys.objects.all()
    # quest = questions.objects.filter(id = F("surveys__question_id")).distinct('question_name')
    quest = surveys.objects.select_related('question')
    # op_sel = options_selection.objects.filter(option_id = F("surveys__answer_sel_id"), question_id = F("surveys__question_id"))
    surv_date = surveys.objects.select_related('answer_date_id')
    surv_opt = surveys.objects.select_related('o_id')
    surv_count = surv_opt.distinct('survey_id')
    dic =  {}
    for o in surv_opt.distinct('survey_id'):
        dic[o.survey_id] = {}
        for s in surv_opt:
            if o.survey_id == s.survey_id:
                q = quest.filter(question_id = s.question_id)[0].question.question_name
                if s.o_id:
                    ans_sel = s.o_id.option_name
                    dic[o.survey_id][q] = ans_sel
                elif s.answer_date_id:
                    da = surv_date.filter(answer_date_id_id = s.answer_date_id_id)[0].answer_date_id.date_value
                    ans_sel = da
                    dic[o.survey_id][q] = ans_sel
    return render(request, 'dappx/doctor.html', {"surv": surv, "quest": quest, "surv_opt":surv_opt, "dic": dic})
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

        # surv = surveys(survey_id = survey_id, question_id = 1, answer_date_id_id = date_ans.id)
        # surv.save()
        for num_quest in range(1, len(quest)+1):
            if quest.values_list('question_type', flat=True).get(pk = num_quest) == 'Date':
                anket_date = request.POST.get("question1_date")
                date_ans = date_answers(date_value = anket_date, question_id = num_quest)
                date_ans.save()
                surv = surveys(survey_id = survey_id, question_id = num_quest, answer_date_id_id = date_ans.id)
                surv.save()
            else:
                option = options_selection.objects.all()
                option_id = request.POST.get("question"+str(num_quest))
                oid = option.filter(option_id = option_id).filter(question_id = num_quest).only('id')[0]
                surv = surveys(survey_id = survey_id, question_id = num_quest,o_id = oid, answer_sel_id= option_id)
                surv.save()
        # question_answer =request.POST['value']#option_id or row_text_answer_id or date_answer_id
        return HttpResponse("Данные успешно загружены в базу данных")